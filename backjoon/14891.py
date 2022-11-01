import sys


def revolve(g, n, d):
    if d == 1:
        e = g[n].pop()
        g[n].insert(0, e)
    else:
        e = g[n].pop(0)
        g[n].append(e)


input = sys.stdin.readline

g = [[]]
for i in range(4):
    g.append(list(map(int, list(input().rstrip()))))
K = int(input())
for i in range(K):
    n, d = map(int, input().rstrip().split(' '))

    connected = [False, g[1][2] != g[2][6], g[2][2] != g[3][6], g[3][2] != g[4][6]]

    revolve(g, n, d)
    right_n = n + 1
    right_d = -d
    while right_n <= 4:
        if not connected[right_n - 1]:
            break
        revolve(g, right_n, right_d)
        right_n += 1
        right_d = -right_d
    left_n = n - 1
    left_d = -d
    while left_n >= 1:
        if not connected[left_n]:
            break
        revolve(g, left_n, left_d)
        left_n -= 1
        left_d = -left_d

score = 0
if g[1][0] == 1:
    score += 1
if g[2][0] == 1:
    score += 2
if g[3][0] == 1:
    score += 4
if g[4][0] == 1:
    score += 8
print(score)
