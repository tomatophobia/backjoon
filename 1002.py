import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if r2 > r1:
        r1, r2 = r2, r1

    if r1 + r2 < d:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif r1 - r2 < d < r1 + r2:
        print(2)
    elif r1 - r2 == d:
        print(1)
    else:
        print(0)
