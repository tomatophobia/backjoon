import sys
import math

input = sys.stdin.readline

N = int(input().rstrip())

A = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    A.append(line)

dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[False] * N for _ in range(N)]
x, y = N // 2, N // 2
visited[x][y] = True
d = 0
out = 0
for _ in range(N * N - 1):
    d = (d + 1) % 4
    dx, dy = x + dirs[d][0], y + dirs[d][1]
    if visited[dx][dy]:
        d = (d - 1) % 4
        dx, dy = x + dirs[d][0], y + dirs[d][1]
    x, y = dx, dy
    visited[x][y] = True

    sand = A[x][y]
    left = sand
    l = [
        [[1, -1, 1], [1, 1, 1], [0, -1, 7], [0, 1, 7], [-1, -1, 10], [-1, 1, 10], [-2, 0, 5], [0, -2, 2], [0, 2, 2]],
        [[-1, 1, 1], [1, 1, 1], [-1, 0, 7], [1, 0, 7], [-1, -1, 10], [1, -1, 10], [0, -2, 5], [-2, 0, 2], [2, 0, 2]],
        [[-1, -1, 1], [-1, 1, 1], [0, -1, 7], [0, 1, 7], [1, -1, 10], [1, 1, 10], [2, 0, 5], [0, -2, 2], [0, 2, 2]],
        [[-1, -1, 1], [1, -1, 1], [-1, 0, 7], [1, 0, 7], [-1, 1, 10], [1, 1, 10], [0, 2, 5], [-2, 0, 2], [2, 0, 2]],
         ]
    for a, b, p in l[d]:
        dust = math.floor(sand * p / 100)
        left -= dust
        if 0 <= x + a < N and 0 <= y + b < N:
            A[x + a][y + b] += dust
        else:
            out += dust
    if 0 <= x + dirs[d][0] < N and 0 <= y + dirs[d][1] < N:
        A[x + dirs[d][0]][y + dirs[d][1]] += left
    else:
        out += left
    A[x][y] = 0
print(out)
