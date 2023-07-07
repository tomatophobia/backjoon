import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

i = 0
for r in range(N):
    for c in range(M):
        if board[r][c] != 1:
            continue
        i += 1
        start = [r, c]
        board[r][c] = -i
        queue = deque([start])
        while len(queue) > 0:
            x, y = queue.popleft()
            for dr, dc in dirs:
                dx, dy = x + dr, y + dc
                if dx < 0 or dx >= N or dy < 0 or dy >= M or board[dx][dy] <= 0:
                    continue
                board[dx][dy] = -i
                queue.append([dx, dy])

graph = [[float('inf')] * (i + 1) for _ in range(i + 1)]

for r in range(N):
    for c in range(M):
        if board[r][c] >= 0:
            continue
        u = -board[r][c]
        for dr, dc in dirs:
            v = None
            dx, dy = r, c
            count = 0
            while True:
                dx, dy = dx + dr, dy + dc
                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                    break
                if board[dx][dy] < 0:
                    v = -board[dx][dy]
                    break
                count += 1
            if v is None or u == v or count <= 1:
                continue
            if count < graph[u][v]:
                graph[u][v] = count

heap = []
heappush(heap, [0, 1])
visited = [False] * (i + 1)
count = 0
mst_weight = 0
while len(heap) > 0:
    w, u = heappop(heap)
    if visited[u]:
        continue
    count += 1
    mst_weight += w

    visited[u] = True

    for v in range(1, i + 1):
        if graph[u][v] < float('inf') and not visited[v]:
            heappush(heap, [graph[u][v], v])

if count != i:
    print(-1)
else:
    print(mst_weight)
