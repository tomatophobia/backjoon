import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

connected = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().rstrip().split(' '))
    connected[x][y] = True
    connected[y][x] = True

visited = [False] * (N + 1)
visited[0] = True

count = 0
while False in visited:
    count += 1
    queue = deque([visited.index(False)])
    while len(queue) > 0:
        v = queue.popleft()
        if visited[v]:
            continue
        visited[v] = True
        for w in range(1, N + 1):
            if not connected[v][w]:
                continue
            queue.append(w)
print(count)
