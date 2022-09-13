import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(' '))

dq = deque([i for i in range(1, n + 1)])

result = []

while len(dq) > 0:
    for i in range(k):
        dq.append(dq.popleft())
    result.append(str(dq.pop()))
print('<' + str.join(', ', result) + '>')

# 더 빠른 방법 있나?

'''
1등의 픽. pop(i)를 써서 속도는 비슷할 것 같은데 더 간결하다
N, K = map(int, input().split())
l = list(range(1, N+1))
p = list()
i = 0
while l:
    i = (i+K-1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')
'''
