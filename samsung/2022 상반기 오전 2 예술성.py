import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

four = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def evaluate(board, N):
    groups = []
    group_idx = -1
    visited = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] >= 0:
                continue
            group_idx += 1
            visited[r][c] = group_idx
            queue = deque([[r, c]])
            graph = [[r, c]]
            group_num = board[r][c]
            while len(queue) > 0:
                x, y = queue.popleft()
                for dx, dy in four:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] == group_num:
                        visited[nx][ny] = group_idx
                        queue.append([nx, ny])
                        graph.append([nx, ny])
            groups.append([group_num, graph])
    # 그룹 간 연결관계 구하기
    edge = [[0] * len(groups) for _ in range(len(groups))]
    for group_idx in range(len(groups)):
        group_num, graph = groups[group_idx]
        for vx, vy in graph:
            for dx, dy in four:
                nx, ny = vx + dx, vy + dy
                if 0 <= nx < N and 0 <= ny < N and group_idx != visited[nx][ny]:
                    edge[group_idx][visited[nx][ny]] += 1
                    edge[visited[nx][ny]][group_idx] += 1
    score = 0
    for x in range(len(groups) - 1):
        for y in range(x + 1, len(groups)):
            if edge[x][y] > 0:
                xgn, xgraph = groups[x]
                ygn, ygraph = groups[y]
                score += (len(xgraph) + len(ygraph)) * xgn * ygn * (edge[x][y] // 2)
    return score


def rotate(board, N):  # O(N^2)
    new_board = [[0] * N for _ in range(N)]
    # 십자 회전
    for r in range(N):
        new_board[N//2][r] = board[r][N//2]
    for c in range(N):
        new_board[N - c - 1][N//2] = board[N//2][c]
    # 나머지 회전
    # 평행이동 -> 시계 90도 -> 평행이동
    # 좌상
    k = N // 2
    for r in range(N//2):
        for c in range(N//2):
            new_board[c][k - 1 - r] = board[r][c]
    # 우상
    for r in range(N//2):
        for c in range(N//2 + 1, N):
            new_board[c - k - 1][2 * k - r] = board[r][c]
    # 좌하
    for r in range(N//2 + 1, N):
        for c in range(N//2):
            new_board[c + k + 1][2 * k - r] = board[r][c]
    # 우하
    for r in range(N//2 + 1, N):
        for c in range(N//2 + 1, N):
            new_board[c][3 * k - r + 1] = board[r][c]
    return new_board


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))

total_score = 0
# 초기 예술 점수
total_score += evaluate(board, N)

for _ in range(3):
    # 회전
    board = rotate(board, N)
    # 예술 점수 구하기
    total_score += evaluate(board, N)
print(total_score)
