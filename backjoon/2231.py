import sys

input = sys.stdin.readline

n = int(input())

exist = False
for i in range(1, n):
    si = str(i)
    sumi = i
    for s in si:
        sumi += int(s)
    if sumi == n:
        exist = True
        print(i)
        break
if not exist:
    print(0)
