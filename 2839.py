import sys

input = sys.stdin.readline

x = int(input())

a = x // 5
r = x % 5

while r % 3 != 0 and a > 0:
    r += 5
    a -= 1

if r % 3 != 0:
    print(-1)
else:
    print(a + r // 3)
