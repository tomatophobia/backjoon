"""
채점 기준 너무 빡빡해서 시간 초과남. 해당 코드 말고 다른 코드로 제출함. 시간 복잡도 측면에서는 해당 코드도 정답
"""
import sys
from itertools import permutations
from collections import deque

# sys.stdin=open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())

scores = [[] for _ in range(8)]
first = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    for i in range(1, 9):
        scores[i - 1].append(line[i])
    first.append(line[0])

max_score = 0
for case in permutations(scores):
    case = list(case)
    case.insert(3, first)
    score = 0
    inning = 0
    turn = 0
    runners = deque([False, False, False])
    out_count = 0
    while inning < N:
        hit = case[turn][inning]
        if hit > 0:
            runners.append(True)
            for _ in range(hit - 1):
                runners.append(False)
            for _ in range(hit):
                if runners.popleft():
                    score += 1
        else:
            out_count += 1
        if out_count == 3:
            out_count = 0
            runners = deque([False, False, False])
            inning += 1
        turn = (turn + 1) % 9
    if score > max_score:
        max_score = score
print(max_score)
