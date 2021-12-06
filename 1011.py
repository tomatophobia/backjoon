import sys
import math

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split(" "))
    d = b - a

    # n^2 + n >= d 가 되는 정수 n의 최솟값. n은 작동 횟수의 반복 횟수
    n = math.ceil((-1 + math.sqrt(1 + 4 * d)) / 2)

    if d <= n * n:
        print(2 * n - 1)
    else:
        print(2 * n)
