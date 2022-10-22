import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(' '))

visited = [False for _ in range(100001)]
pre = [None for _ in range(100001)]
pre[n] = -1
queue = deque([n])
while len(queue) > 0:
    v = queue.popleft()
    if visited[v]:
        continue
    visited[v] = True
    if v == k:
        break
    next = [v + 1, v - 1, 2 * v]
    for nv in next:
        if nv < 0 or nv > 100000:
            continue
        if pre[nv] is None:
            pre[nv] = v
        queue.append(nv)
s = pre[k]
c = 0
while s != -1:
    c += 1
    s = pre[s]
print(c)
