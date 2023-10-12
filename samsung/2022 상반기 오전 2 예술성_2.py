import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def get_score(board, N):
    four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[False] * N for _ in range(N)]
    graphs = []
    graph_board = [[-1] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            the_num = board[x][y]
            queue = deque([[x, y]])
            visited[x][y] = True
            graph = [[x, y]]
            graph_board[x][y] = len(graphs)
            while len(queue) > 0:
                cx, cy = queue.popleft()
                for dx, dy in four:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] == the_num:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        graph.append([nx, ny])
                        graph_board[nx][ny] = len(graphs)
            graphs.append(graph)
    edges = [[0] * len(graphs) for _ in range(len(graphs))]
    for gi in range(len(graphs)):
        graph = graphs[gi]
        for x, y in graph:
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if not is_valid(nx, ny, N) or graph_board[nx][ny] == gi:
                    continue
                otheri = graph_board[nx][ny]
                edges[gi][otheri] += 1
    score = 0
    for i in range(len(graphs) - 1):
        for j in range(i + 1, len(graphs)):
            if len(graphs[i]) == 0 or len(graphs[j]) == 0 or edges[i][j] == 0:
                continue
            i_num = board[graphs[i][0][0]][graphs[i][0][1]]
            j_num = board[graphs[j][0][0]][graphs[j][0][1]]
            score += (len(graphs[i]) + len(graphs[j])) * i_num * j_num * edges[i][j]
    return score


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
# 초기 예술 점수
score = get_score(board, N)
for _ in range(3):
    # 회전
    # 십자 회전
    next_board = [board[i][:] for i in range(N)]
    for x in range(N):
        next_board[N - 1 - N // 2][x] = board[x][N // 2]
    for y in range(N):
        next_board[N - 1 - y][N // 2] = board[N // 2][y]
    board = next_board
    # 작은 정사각형 4개 회전
    next_board = [board[i][:] for i in range(N)]
    K = N // 2
    for x in range(K):
        for y in range(K):
            next_board[y][K - 1 - x] = board[x][y]
    for x in range(K + 1, N):
        for y in range(K):
            next_board[y + K + 1][K - x + K] = board[x][y]
    for x in range(K):
        for y in range(K + 1, N):
            next_board[y - K - 1][K - x + K] = board[x][y]
    for x in range(K + 1, N):
        for y in range(K + 1, N):
            next_board[y][K - x + K + K + 1] = board[x][y]
    board = next_board
    # 예술 점수
    score += get_score(board, N)
print(score)
