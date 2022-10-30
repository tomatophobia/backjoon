import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().rstrip().split(' ')))
four = list(map(int, input().rstrip().split(' ')))

maxv = -float('inf')
minv = float('inf')
pos1 = [i for i in range(N - 1)]
plus_all = list(combinations(pos1, four[0]))
for plus_pos in plus_all:
    pos2 = list(filter(lambda x: x not in plus_pos, pos1))
    minus_all = list(combinations(pos2, four[1]))
    for minus_pos in minus_all:
        pos3 = list(filter(lambda x: x not in minus_pos, pos2))
        multiply_all = list(combinations(pos3, four[2]))
        for multiply_pos in multiply_all:
            divide_pos = list(filter(lambda x: x not in multiply_pos, pos3))
            v = A[0]
            for i in range(N - 1):
                if i in plus_pos:
                    v += A[i + 1]
                elif i in minus_pos:
                    v -= A[i + 1]
                elif i in multiply_pos:
                    v *= A[i + 1]
                elif i in divide_pos:
                    if v < 0 and A[i + 1] >= 0:
                        v = - ((-v) // A[i + 1])
                    else:
                        v //= A[i + 1]
            if v > maxv:
                maxv = v
            if v < minv:
                minv = v
print(maxv)
print(minv)
