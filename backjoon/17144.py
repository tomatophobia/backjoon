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
    for r in range(R):
        for c in range(C):
            dust = A[r][c]
            if dust < 5:
                temp[r][c] = dust
                continue
            diff = dust // 5
            for d in directions:
                dr = r + d[0]
                dc = c + d[1]
                if dr < 0 or dr >= R or dc < 0 or dc >= C or A[dr][dc] == -1:
                    continue
                temp[dr][dc] += diff
                dust -= diff
            temp[r][c] = dust

    tt = temp[c1][1]
    for i in range(2, C):
        tt, temp[c1][i] = temp[c1][i], tt
    for i in range(c1, -1, -1):
        tt, temp[i][C-1] = temp[i][C-1], tt
    for i in range(C-1, -1, -1):
        tt, temp[0][i] = temp[0][i], tt

# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))