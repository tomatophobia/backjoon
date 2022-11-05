import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(' '))

energy = [[[5, deque()] for _ in range(N)] for _ in range(N)]

A = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    A.append(line)

for _ in range(M):
    x, y, z = map(int, input().rstrip().split(' '))
    x -= 1
    y -= 1
    energy[x][y][1].append(z)

directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
for _ in range(K):
    # 봄, 여름, 겨울
    for i in range(N):
        for j in range(N):
            trees = energy[i][j][1]
            if len(trees) > 0:
                enough = True
                temp = []
                for age in trees:
                    if enough and energy[i][j][0] < age:
                        enough = False
                    if enough:
                        energy[i][j][0] -= age
                        temp.append(age + 1)
                    else:
                        energy[i][j][0] += age // 2
                energy[i][j][1] = deque(temp)
            energy[i][j][0] += A[i][j]
    # 가을
    for i in range(N):
        for j in range(N):
            trees = energy[i][j][1]
            for age in trees:
                if age % 5 == 0:
                    for d in directions:
                        dx = i + d[0]
                        dy = j + d[1]
                        if dx < 0 or dx >= N or dy < 0 or dy >= N:
                            continue
                        energy[dx][dy][1].appendleft(1)

count = 0
for i in range(N):
    for j in range(N):
        count += len(energy[i][j][1])
print(count)
