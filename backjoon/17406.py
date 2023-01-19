import sys
from itertools import permutations

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(' '))

origin = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    origin.append(line)
ops = []
for _ in range(K):
    r, c, s = map(int, input().rstrip().split(' '))
    r, c = r - 1, c - 1
    ops.append([r, c, s])

min_val = float('inf')
for case in permutations(ops):
    A = [origin[i][:] for i in range(N)]
    for r, c, s in case:
        for p in range(1, s + 1):
            temp = A[r - p][c - p]
            for i in range(c - p + 1, c + p + 1):
                A[r - p][i], temp = temp, A[r - p][i]
            for i in range(r - p + 1, r + p + 1):
                A[i][c + p], temp = temp, A[i][c + p]
            for i in range(c + p - 1, c - p - 1, -1):
                A[r + p][i], temp = temp, A[r + p][i]
            for i in range(r + p - 1, r - p - 1, -1):
                A[i][c-p], temp = temp, A[i][c-p]
    val = min(map(sum, A))
    if val < min_val:
        min_val = val
print(min_val)
