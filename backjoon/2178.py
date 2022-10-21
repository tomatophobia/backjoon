import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))

maze = [[]]
for i in range(n):
    line = '0' + input().strip()
    maze.append(list(map(int, list(line))))

f = [[1, 0], [0, 1], [-1, 0], [0, -1]]

predecessors = [[None] * (m + 1) for i in range(n + 1)]
visited = [[False] * (m + 1) for i in range(n + 1)]
queue = deque([[[1, 1], None]])
while len(queue) > 0:
    v, pre = queue.popleft()
    if visited[v[0]][v[1]]:
        continue
    visited[v[0]][v[1]] = True
    predecessors[v[0]][v[1]] = pre
    if v[0] == n and v[1] == m:
        break
    for d in f:
        adj = [v[0] + d[0], v[1] + d[1]]
        if adj[0] < 1 or adj[0] > n or adj[1] < 1 or adj[1] > m or maze[adj[0]][adj[1]] == 0:
            continue
        queue.append([adj, v])

s = [n, m]
p = 0
while s is not None:
    s = predecessors[s[0]][s[1]]
    p += 1
print(p)
