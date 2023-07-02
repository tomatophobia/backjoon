import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

ladders = [None] * 101
for _ in range(N):
    u, v = map(int, input().rstrip().split(' '))
    ladders[u] = v

snakes = [None] * 101
for _ in range(M):
    u, v = map(int, input().rstrip().split(' '))
    snakes[u] = v

start = 1

queue = deque([[start, 0]])

while len(queue) > 0:
    pos, roll = queue.popleft()
    if pos >= 100:
        print(roll)
        break

    if pos + 6 >= 100:
        print (roll + 1)
        break

    no_ladder_snake = True
    for i in range(6, 0, -1):
        next_pos = pos + i
        if next_pos < 100 and ladders[next_pos] is not None:
            next_pos = ladders[next_pos]
            queue.append([next_pos, roll + 1])
        elif next_pos < 100 and snakes[next_pos] is not None:
            next_pos = snakes[next_pos]
            queue.append([next_pos, roll + 1])
        elif no_ladder_snake:
            queue.append([next_pos, roll + 1])
            no_ladder_snake = False
