import sys

input = sys.stdin.readline


def fun(p, rs, re, cs, ce):
    color = p[rs][cs]
    uni = True
    for i in range(rs, re):
        for j in range(cs, ce):
            if color != p[i][j]:
                uni = False
                break
        if not uni:
            break
    if uni:
        if color == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        sumall = [0, 0]
        x, y = fun(p, rs, rs + (re - rs) // 2, cs, cs + (ce - cs) // 2)
        sumall[0] += x
        sumall[1] += y
        x, y = fun(p, rs + (re - rs) // 2, re, cs, cs + (ce - cs) // 2)
        sumall[0] += x
        sumall[1] += y
        x, y = fun(p, rs, rs + (re - rs) // 2, cs + (ce - cs) // 2, ce)
        sumall[0] += x
        sumall[1] += y
        x, y = fun(p, rs + (re - rs) // 2, re, cs + (ce - cs) // 2, ce)
        sumall[0] += x
        sumall[1] += y
        return sumall[0], sumall[1]


n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split(' '))))

w, b = fun(paper, 0, n, 0, n)
print(w)
print(b)
