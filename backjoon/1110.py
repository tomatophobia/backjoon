import sys

input = sys.stdin.readline

n = int(input())

start = n

cnt = 1
while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = b * 10 + c

    if n == start:
        break
    cnt += 1
print(cnt)
