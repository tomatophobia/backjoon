import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

lab = []
candidate = []
num_of_zero = 0
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    for j in range(N):
        if line[j] == 2:
            candidate.append((i, j))
            line[j] = 3
        elif line[j] == 0:
            num_of_zero += 1
    lab.append(line)
if not num_of_zero:
    print(0)
    exit(0)

init_lab = [[lab[i][j] for j in range(N)] for i in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min_t = float('inf')
for viruses in combinations(candidate, M):
    lab = [[init_lab[i][j] for j in range(N)] for i in range(N)]
    left_zero = num_of_zero
    for virus in viruses:
        lab[virus[0]][virus[1]] = 2
    t = 0
    while left_zero > 0 and len(viruses) > 0:
        if t == min_t:
            break
        temp = []
        for i, j in viruses:
            for d in directions:
                di = i + d[0]
                dj = j + d[1]
                if di < 0 or di >= N or dj < 0 or dj >= N or lab[di][dj] == 1 or lab[di][dj] == 2:
                    continue
                if lab[di][dj] == 0:
                    left_zero -= 1
                lab[di][dj] = 2
                temp.append((di, dj))
        viruses = temp
        t += 1
    if left_zero == 0:
        if min_t > t:
            min_t = t

print(min_t if min_t != float('inf') else -1)
