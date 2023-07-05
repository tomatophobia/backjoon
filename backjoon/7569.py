import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split(' '))

board = [[] for _ in range(H)]
start = []
for h in range(H):
    for n in range(N):
        line = list(map(int, input().rstrip().split(' ')))
        for m in range(M):
            if line[m] == 1:
                start.append([h, n, m])
        board[h].append(line)

dirs = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

count = -1
while len(start) > 0:
    next_start = []
    for h, n, m in start:
        for d1, d2, d3 in dirs:
            dh, dn, dm = h + d1, n + d2, m + d3
            if dh < 0 or dh >= H or dn < 0 or dn >= N or dm < 0 or dm >= M or board[dh][dn][dm] != 0:
                continue
            board[dh][dn][dm] = 1
            next_start.append([dh, dn, dm])
    start = next_start
    count += 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if board[h][n][m] == 0:
                print(-1)
                exit(0)
print(count)
