import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split(' '))
A = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    A.append(line)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
days = 0
while True:
    visited = [False] * (N * N)
    moved = False
    # while visited에 False가 있을 때 까지가 아니고 그냥 반복을 돌린 것이 주요했음...
    for r in range(N):
        for c in range(N):
            if visited[N * r + c]:
                continue
            union = []
            union_count = 0
            union.append((r, c))
            union_count += A[r][c]
            queue = deque([(r, c)])
            visited[N * r + c] = True
            while len(queue) > 0:
                x, y = queue.popleft()
                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    didx = dx * N + dy
                    if dx < 0 or dx >= N or dy < 0 or dy >= N or visited[didx]:
                        continue
                    if L <= abs(A[x][y] - A[dx][dy]) <= R:
                        queue.append((dx, dy))
                        visited[didx] = True
                        union.append((dx, dy))
                        union_count += A[dx][dy]
            if len(union) > 1:
                moved = True
                avg = union_count // len(union)
                for x, y in union:
                    A[x][y] = avg
    if not moved:
        break
    days += 1
print(days)
