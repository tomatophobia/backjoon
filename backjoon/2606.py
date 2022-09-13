import sys

input = sys.stdin.readline

v = int(input())
e = int(input())

connected = [[False] * (v + 1) for _ in range(v + 1)]

for i in range(e):
    v1, v2 = map(int, input().split(' '))
    connected[v1][v2] = True
    connected[v2][v1] = True

stack = [1]
visited = [False] * (v + 1)
count = 0
while len(stack) > 0:
    cur = stack.pop()
    if not visited[cur]:
        visited[cur] = True
        count += 1
        for i in range(len(connected[cur]) - 1, 0, -1):
            if connected[cur][i] and not visited[i]:
                stack.append(i)
print(count - 1)
