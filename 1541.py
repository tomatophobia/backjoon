import sys

input = sys.stdin.readline

exp = input().rstrip()

ans = 0
tok = ''
minus = False
for i in exp:
    if i == '+' or i == '-':
        if minus:
            ans -= int(tok)
        else:
            ans += int(tok)
        tok = ''
        if i == '-':
            minus = True
    else:
        tok += i

if minus:
    ans -= int(tok)
else:
    ans += int(tok)
tok = ''

print(ans)

'''
증명?
-a1 + a2 + a3 + ... + ak 수열로 가능한 최솟값이 -(a1 + ... + ak) 이므로 그것보다 더 최소가 나올 수 없으니까 Greedy가 맞다? 이렇게 증명?
'''
