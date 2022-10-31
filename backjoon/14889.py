import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    S.append(line)

min_diff = float('inf')
all = [i + 1 for i in range(N)]
team1_all = list(combinations(all, N // 2))
for team1 in team1_all:
    team2 = filter(lambda x: x not in team1, all)
    score1 = 0
    score2 = 0
    for x, y in list(combinations(team1, 2)):
        score1 += S[x-1][y-1] + S[y-1][x-1]
    for x, y in list(combinations(team2, 2)):
        score2 += S[x-1][y-1] + S[y-1][x-1]
    diff = abs(score1 - score2)
    if diff < min_diff:
        min_diff = diff
print(min_diff)
