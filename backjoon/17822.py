import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().rstrip().split(' '))

circles = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    circles.append(line)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cmd = []
for _ in range(T):
    x, d, k = map(int, input().rstrip().split(' '))
    k = k % M
    if d == 0:
        k = -k
    for i in range(N):
        if (i + 1) % x == 0:
            circles[i] = circles[i][k:] + circles[i][:k]
    erased = False
    for i in range(N):
        for j in range(M):
            e = circles[i][j]
            if e == 0:
                continue
            graph = []
            visited = [[False] * M for _ in range(N)]
            queue = deque([(i, j)])
            visited[i][j] = True
            graph.append((i, j))
            while len(queue) > 0:
                x, y = queue.pop()
                for d in dirs:
                    dx, dy = x + d[0], (y + d[1] + M) % M
                    if dx < 0 or dx >= N or circles[dx][dy] == 0 or circles[dx][dy] != e or visited[dx][dy]:
                        continue
                    queue.append((dx, dy))
                    visited[dx][dy] = True
                    graph.append((dx, dy))
            if len(graph) > 1:
                for x, y in graph:
                    circles[x][y] = 0
                erased = True
    if not erased:
        s = 0
        c = 0
        for x in range(N):
            for y in range(M):
                if circles[x][y] > 0:
                    s += circles[x][y]
                    c += 1
        if c != 0:
            avg = s / c
            for x in range(N):
                for y in range(M):
                    if circles[x][y] == 0:
                        continue
                    if circles[x][y] > avg:
                        circles[x][y] -= 1
                    elif circles[x][y] < avg:
                        circles[x][y] += 1

s = 0
for i in range(N):
    for j in range(M):
        s += circles[i][j]
print(s)
