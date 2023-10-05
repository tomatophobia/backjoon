import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def print_board(board):
    print("---")
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def board_gravity(board, N):
    for c in range(N):
        for r in range(N - 2, -1, -1):
            if board[r][c] < 0:
                continue
            x, y = r, c
            nx, ny = x + 1, y
            while is_valid(nx, ny, N) and board[nx][ny] == -2:
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                x, y = nx, ny
                nx, ny = x + 1, y
    return board


four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
score = 0
while True:
    # 폭탄그룹
    groups = []  # [그룹 크기 큰 순, red 작은 순, 행 큰 순, 열 작은 순, 그룹]
    visited = [[False] * N for _ in range(N)]
    for r in range(N - 1, -1, -1):
        for c in range(N):
            if board[r][c] <= 0 or visited[r][c]:
                continue
            reds, start, group = [], [r, c], [[r, c]]
            visited[r][c] = True
            queue = deque([start])
            while len(queue) > 0:
                x, y = queue.popleft()
                for dx, dy in four:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, N) and not visited[nx][ny] and (
                            board[nx][ny] == board[r][c] or board[nx][ny] == 0):
                        if board[nx][ny] == 0:
                            reds.append([nx, ny])
                        group.append([nx, ny])
                        visited[nx][ny] = True
                        queue.append([nx, ny])
            for rx, ry in reds:
                visited[rx][ry] = False
            if len(group) > 1:
                groups.append([len(group), -len(reds), start[0], -start[1], group])
    if len(groups) == 0:
        break
    # 폭발
    best = max(groups)[4]
    score += len(best) ** 2
    for bx, by in best:
        board[bx][by] = -2  # 빈공간
    # 중력
    board = board_gravity(board, N)
    # 90도 반시계 회전
    next_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            next_board[N - 1 - y][x] = board[x][y]
    board = next_board
    # 중력
    board = board_gravity(board, N)

print(score)
