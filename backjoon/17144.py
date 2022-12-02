import sys

input = sys.stdin.readline

R, C, T = map(int, input().rstrip().split(' '))

A = []
c1 = -1
c2 = -1
for i in range(R):
    line = list(map(int, input().rstrip().split(' ')))
    if -1 in line:
        if c1 == -1:
            c1 = i
        else:
            c2 = i
    A.append(line)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(T):
    temp = [[0] * C for _ in range(R)]
    temp[c1][0] = -1
    temp[c2][0] = -1
    for r in range(R):
        for c in range(C):
            if (r == c1 or r == c2) and c == 0:
                continue
            dust = A[r][c]
            if dust < 5:
                temp[r][c] += dust
                continue
            diff = dust // 5
            for d in directions:
                dr = r + d[0]
                dc = c + d[1]
                if dr < 0 or dr >= R or dc < 0 or dc >= C or A[dr][dc] == -1:
                    continue
                temp[dr][dc] += diff
                dust -= diff
            temp[r][c] += dust

    tt = temp[c1][1]
    for i in range(2, C):
        tt, temp[c1][i] = temp[c1][i], tt
    for i in range(c1-1, -1, -1):
        tt, temp[i][C-1] = temp[i][C-1], tt
    for i in range(C-2, -1, -1):
        tt, temp[0][i] = temp[0][i], tt
    for i in range(1, c1):
        tt, temp[i][0] = temp[i][0], tt
    temp[c1][1] = 0
    tt = temp[c2][1]
    for i in range(2, C):
        tt, temp[c2][i] = temp[c2][i], tt
    for i in range(c2+1, R):
        tt, temp[i][C-1] = temp[i][C-1], tt
    for i in range(C-2, -1, -1):
        tt, temp[R-1][i] = temp[R-1][i], tt
    for i in range(R-2, c2, -1):
        tt, temp[i][0] = temp[i][0], tt
    temp[c2][1] = 0

    A = temp

count = 0
for i in range(R):
    for j in range(C):
        if (i == c1 or i == c2) and j == 0:
            continue
        count += A[i][j]
print(count)
