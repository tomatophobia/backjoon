import sys

input = sys.stdin.readline

d = [0 for _ in range(101)]

for i in range(1, 101):
    if i <= 3:
        d[i] = 1
    elif i <= 5:
        d[i] = 2
    else:
        d[i] = d[i-1] + d[i-5]

t = int(input())

for i in range(t):
    n = int(input())
    print(d[n])

'''
d[i] = d[i-1] + d[i-4] 한 번에 삼각형이 60도씩 회전해서 3번 붙으면 평행 선상에 오니까...?
'''
