import sys
from itertools import combinations
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())
people = list(map(int, input().rstrip().split(' ')))
edge = []
for i in range(N):
    line = list(map(lambda x: int(x) - 1, input().rstrip().split(' ')))
    edge.append(line[1:])

vertex = [i for i in range(N)]
min_diff = float('inf')
for number_of_g1 in range(1, N // 2 + 1):
    for case in combinations(vertex, number_of_g1):
        g1 = []
        g2 = []
        k = 0
        for i in range(N):
            if k < len(case) and i == case[k]:
                g1.append(i)
                k += 1
            else:
                g2.append(i)
        # check g1 connected
        queue = deque([g1[0]])
        visited = [False] * N
        visited[g1[0]] = True
        for i in g2:
            visited[i] = True
        while len(queue) > 0:
            x = queue.popleft()
            for y in edge[x]:
                if not visited[y]:
                    visited[y] = True
                    queue.append(y)
        if False in visited:
            continue
        # check g2 connected
        queue = deque([g2[0]])
        visited = [False] * N
        visited[g2[0]] = True
        for i in g1:
            visited[i] = True
        while len(queue) > 0:
            x = queue.popleft()
            for y in edge[x]:
                if not visited[y]:
                    visited[y] = True
                    queue.append(y)
        if False in visited:
            continue
        # get diff
        value_g1 = 0
        for i in g1:
            value_g1 += people[i]
        value_g2 = 0
        for i in g2:
            value_g2 += people[i]
        diff = abs(value_g1 - value_g2)
        if diff < min_diff:
            min_diff = diff
if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)
