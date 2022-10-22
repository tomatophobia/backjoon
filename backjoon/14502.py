import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

lab = []
zeros = []
for i in range(n):
    line = list(map(int, input().rstrip().split()))
    for j in range(m):
        if line[j] == 0:
            zeros.append((i, j))
    lab.append(line)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
max_count = 0
for z3 in combinations(zeros, 3):
    lab1 = [line[:] for line in lab]
    for x, y in z3:
        lab1[x][y] = 1
    queue = []
    for i in range(n):
        for j in range(m):
            if lab1[i][j] == 2:
                queue.append((i, j))
                lab1[i][j] = 0
    while len(queue) > 0:
        temp = []
        for v in queue:
            if lab1[v[0]][v[1]] != 0:
                continue
            lab1[v[0]][v[1]] = 2
            for mv in move:
                x = v[0] + mv[0]
                y = v[1] + mv[1]
                if x < 0 or x >= n or y < 0 or y >= m or lab1[x][y] != 0:
                    continue
                temp.append((x, y))
        queue = temp
    count = 0
    for i in range(n):
        for j in range(m):
            if lab1[i][j] == 0:
                count += 1
    if count > max_count:
        max_count = count
print(max_count)
