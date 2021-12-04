import sys
import math

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split(' '))
    # nCm
    print(int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n))))
