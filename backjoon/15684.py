import sys
from itertools import combinations

input = sys.stdin.readline


def one_to_one(c, h, n):
    success = True
    for i in range(n):
        x, y = 0, i
        while x < h:
            if c[x][y] == 0:
                x, y = x + 1, y
            else:
                x, y = x + 1, y + c[x][y]
        if i != y:
            success = False
            break
    return success


N, M, H = map(int, input().rstrip().split(' '))
connected = [[0] * N for _ in range(H)]
for i in range(M):
    x, y = map(int, input().rstrip().split(' '))
    connected[x - 1][y - 1] = 1
    connected[x - 1][y] = -1

not_connected_pair = []
for i in range(H):
    for j in range(N-1):
        if connected[i][j] == 0 and connected[i][j+1] == 0:
            not_connected_pair.append((i, j))

min_ho = 4
if one_to_one(connected, H, N):
    min_ho = 0

# 1
if min_ho > 1:
    for i, j in not_connected_pair:
        connected_copy = [l[:] for l in connected]
        connected_copy[i][j] = 1
        connected_copy[i][j + 1] = -1
        if one_to_one(connected_copy, H, N):
            min_ho = 1
            break

# 2
if min_ho > 2:
    for pairs in list(combinations(not_connected_pair, 2)):
        i, j = pairs[0]
        p, q = pairs[1]
        connected_copy = [l[:] for l in connected]
        connected_copy[i][j] = 1
        connected_copy[i][j + 1] = -1
        connected_copy[p][q] = 1
        connected_copy[p][q + 1] = -1
        if one_to_one(connected_copy, H, N):
            min_ho = 2
            break


# 3
if min_ho > 3:
    for pairs in list(combinations(not_connected_pair, 3)):
        i, j = pairs[0]
        p, q = pairs[1]
        r, s = pairs[2]
        connected_copy = [l[:] for l in connected]
        connected_copy[i][j] = 1
        connected_copy[i][j + 1] = -1
        connected_copy[p][q] = 1
        connected_copy[p][q + 1] = -1
        connected_copy[r][s] = 1
        connected_copy[r][s + 1] = -1
        if one_to_one(connected_copy, H, N):
            min_ho = 3
            break

if min_ho > 3:
    print(-1)
else:
    print(min_ho)
