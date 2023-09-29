import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

cross = []
for _ in range(M):
    u, v = map(int, input().rstrip().split(' '))
    cross.append([u - 1, v - 1])

t = 0
cursor = [False] * N
cursor[0] = True
while not cursor[-1]:
    u, v = cross[t % M]
    if cursor[u]:
        cursor[v] = True
    if cursor[v]:
        cursor[u] = True
    t += 1
print(t)

## sparse 그래프이기 때문에 다익스트라를 써야 하나보다.
