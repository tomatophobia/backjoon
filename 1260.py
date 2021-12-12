import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split(' '))

matrix = [[0] * (n + 1) for i in range(n + 1)]  # one-index

for i in range(m):
    v1, v2 = map(int, input().split(' '))
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1  # XXX 주의 adjacency matrix는 양쪽에 다 넣어주자

# DFS
stack = [v]
result = []
visited = [False] * (n + 1)
while len(stack) > 0:
    curr = stack.pop()
    if not visited[curr]:
        visited[curr] = True
        result.append(str(curr))
        for i in range(len(matrix[curr]) - 1, 0, -1):
            if matrix[curr][i] == 1 and not visited[i]:
                stack.append(i)
print(' '.join(result))

# BFS
queue = deque([v])
result = [str(v)]
visited = [False] * (n + 1)
visited[v] = True
while len(queue) > 0:
    curr = queue.popleft()
    for i in range(1, len(matrix[curr])):
        if matrix[curr][i] == 1 and not visited[i]:
            result.append(str(i))
            visited[i] = True
            queue.append(i)
print(' '.join(result))
