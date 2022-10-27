import math
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split(' ')))
B, C = map(int, input().rstrip().split(' '))

count = 0
for i in A:
    if B >= i:
        count += 1
    else:
        x = math.ceil((i - B) / C)
        count += x + 1
print(count)
