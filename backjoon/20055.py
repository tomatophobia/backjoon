import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split(' '))

A = list(map(int, input().rstrip().split(' ')))

count = 0
cursor = 0
robots = []
while K > 0:
    count += 1
    cursor = (cursor + 2 * N - 1) % (2 * N)
    end = (cursor + N - 1) % (2 * N)
    if end in robots:
        robots.remove(end)
    i = 0
    while i < len(robots):
        r = robots[i]
        dr = (r + 1) % (2 * N)
        if dr in robots or A[dr] == 0:
            i += 1
            continue
        A[dr] -= 1
        if dr == end:
            robots.remove(r)
            i -= 1
        else:
            robots[i] = dr
        if A[dr] == 0:
            K -= 1
        i += 1
    if A[cursor] > 0:
        robots.append(cursor)
        A[cursor] -= 1
        if A[cursor] == 0:
            K -= 1
print(count)
