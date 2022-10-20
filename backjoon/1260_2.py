import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split(' '))

connected = [[False] * (n + 1) for i in range(n + 1)]  # one-index

for i in range(m):
    x, y = map(int, input().split(' '))
    connected[x][y] = True
    connected[y][x] = True

# DFS
stack = [v]
visited = [False for i in range(n + 1)]
result = []
while len(stack) != 0:
    x = stack.pop()
    if not visited[x]:
        visited[x] = True
        result.append(str(x))
        for y in range(n, 0, -1):
            if connected[x][y] and not visited[y]:
                stack.append(y)
print(' '.join(result))

# BFS
queue = deque([v])
visited = [False for i in range(n + 1)]
result = []
while len(queue) != 0:
    x = queue.popleft()
    if not visited[x]:
        visited[x] = True
        result.append(str(x))
        for y in range(1, n+1):
            if connected[x][y] and not visited[y]:
                queue.append(y)
print(' '.join(result))
