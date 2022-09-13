import sys

input = sys.stdin.readline

n = int(input())

sum = 0
mmax = -4000
mmin = 4000
appear = [0] * 8001
l = []
for _ in range(n):
    x = int(input())
    sum += x
    if x > mmax:
        mmax = x
    if x < mmin:
        mmin = x
    appear[x + 4000] += 1
    l.append(x)

l.sort()
print(round(sum / len(l)))
print(l[len(l) // 2])
a = max(appear)
c1 = appear.index(a)
c2 = -1
if a in appear[c1 + 1:]:
    c2 = appear[c1 + 1:].index(a) + c1 + 1
if c2 == -1:
    print(c1 - 4000)
else:
    print(c2 - 4000)
print(mmax - mmin)

'''
버림과 반올림 주의
'''
