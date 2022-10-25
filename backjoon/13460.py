import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

pan = []

R = None
B = None
Z = None
for i in range(N):
    line = list(input())
    if 'R' in line:
        R = (i, line.index('R'))
        line[R[1]] = '.'
    if 'B' in line:
        B = (i, line.index('B'))
        line[B[1]] = '.'
    if 'O' in line:
        Z = (i, line.index('O'))
        line[Z[1]] = '.'
    pan.append((line))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stack = [(R, B, 0)]
min_depth = 11
while len(stack) > 0:
    r, b, depth = stack.pop()
    if depth >= min_depth - 1:
        continue
    for d in directions:
        R = r
        B = b
        while True:
            NR = R
            NB = B
            # R 한 칸 움직임
            if R is not None and pan[R[0] + d[0]][R[1] + d[1]] == '.':
                NR = (R[0] + d[0], R[1] + d[1])
            # B 한 칸 움직임
            if B is not None and pan[B[0] + d[0]][B[1] + d[1]] == '.':
                NB = (B[0] + d[0], B[1] + d[1])
            # 구슬끼리 겹치면 멈춤
            if (R is not None and B is not None) and NR == NB:
                break
            # 두 구슬 다 움직이지 않으면 멈춤
            if (R is None or R == NR) and (B is None or B == NB):
                break
            # 구슬이 0을 지나면 빠져나감
            if NR == Z:
                NR = None
            if NB == Z:
                NB = None
            R = NR
            B = NB
        if R is not None and B is not None:
            stack.append((R, B, depth + 1))
        elif R is None and B is not None:  # 성공
            if min_depth > depth + 1:
                min_depth = depth + 1
if min_depth > 10:
    print(-1)
else:
    print(min_depth)
