import sys

sys.stdin = open('input.txt', 'r')

import math


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


four = [[0, -1], [1, 0], [0, 1], [-1, 0]]
N = int(input().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))

x, y, d = N // 2, N // 2, 0
visited = [[False] * N for _ in range(N)]
visited[x][y] = True

count = 0
while True:
    nx, ny = x + four[d][0], y + four[d][1]
    if not is_valid(nx, ny, N):
        break
    visited[nx][ny] = True
    x, y = nx, ny
    # 먼지 퍼지기
    left = board[x][y]
    target = [[1, [[d - 2, d + 1], [d - 2, d - 1]]], [2, [[d + 1, d + 1], [d - 1, d - 1]]], [5, [[d, d]]],
              [7, [[d + 1], [d - 1]]], [10, [[d, d + 1], [d, d - 1]]]]
    for percentage, moves_list in target:
        for moves in moves_list:
            dust = math.floor(board[x][y] * percentage / 100)
            left -= dust
            nx, ny = x, y
            for mv in moves:
                mvd = mv % 4
                nx, ny = nx + four[mvd][0], ny + four[mvd][1]
            if is_valid(nx, ny, N):
                board[nx][ny] += dust
            else:
                count += dust
    nx, ny = x + four[d][0], y + four[d][1]
    if is_valid(nx, ny, N):
        board[nx][ny] += left
    else:
        count += left
    board[x][y] = 0
    # 꺾어보기
    nd = (d + 1) % 4
    nx, ny = x + four[nd][0], y + four[nd][1]
    if visited[nx][ny]:
        nd = d
    d = nd
print(count)
