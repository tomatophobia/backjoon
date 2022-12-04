import argparse
import sys

input = sys.stdin.readline

r, c, k = map(int, input().rstrip().split(' '))
r = r - 1
c = c - 1

A = []
for _ in range(3):
    l = list(map(int, input().rstrip().split(' ')))
    A.append(l)

t = 0
while (r < len(A) and c < len(A[r]) and A[r][c]) != k and t < 100:
    nr = len(A)
    nc = len(A[0])
    if nr >= nc:
        mc = 0
        nextA = []
        for i in range(nr):
            nextRow = {}
            for j in range(nc):
                e = A[i][j]
                if e == 0:
                    continue
                if e in nextRow:
                    nextRow[e] = nextRow[e] + 1
                else:
                    nextRow[e] = 1
            nextRow = list(nextRow.items())
            nextRow.sort(key=lambda x: (x[1], x[0]))
            nextRow2 = []
            for a, b in nextRow:
                nextRow2.append(a)
                nextRow2.append(b)
            nextA.append(nextRow2)
            if mc < len(nextRow2):
                mc = len(nextRow2)
        for i in range(nr):
            nextA[i] = nextA[i] + [0] * (mc - len(nextA[i]))
        A = nextA
    else:
        mr = 0
        nextA = []
        for j in range(nc):
            nextCol = {}
            for i in range(nr):
                e = A[i][j]
                if e == 0:
                    continue
                if e in nextCol:
                    nextCol[e] = nextCol[e] + 1
                else:
                    nextCol[e] = 1
            nextCol = list(nextCol.items())
            nextCol.sort(key=lambda x: (x[1], x[0]))
            nextCol2 = []
            for a, b in nextCol:
                nextCol2.append(a)
                nextCol2.append(b)
            nextA.append(nextCol2)
            if mr < len(nextCol2):
                mr = len(nextCol2)
        A = [[0] * nc for _ in range(mr)]
        for i in range(len(nextA)):
            for j in range(len(nextA[i])):
                A[j][i] = nextA[i][j]

    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))
    # print('---')
    t += 1
if r < len(A) and c < len(A[r]) and A[r][c] == k:
    print(t)
else:
    print(-1)
