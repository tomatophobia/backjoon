import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
board = []
house = []
chicken = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))
    board.append(line)

min_city = float('inf')
for chi in list(combinations(chicken, M)):
    city = 0
    for hx, hy in house:
        cd = float('inf')
        for cx, cy in chi:
            d = abs(cx - hx) + abs(cy - hy)
            if d < cd:
                cd = d
        city += cd
    if city < min_city:
        min_city = city
print(min_city)
