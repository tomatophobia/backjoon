import sys
import math

input = sys.stdin.readline

a, b, c = map(int, input().split(' '))

if b < c:
    print(math.floor(a / (c-b) + 1))
else:
    print(-1)
