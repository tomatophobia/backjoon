import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    x, y = map(int, input().rstrip().split(' '))
    board[x-1][y-1] = 1

L = int(input())
paths = []
for i in range(L):
    x, c = input().rstrip().split(' ')
    paths.append((int(x), c))
paths.append((float('inf'), 'E'))  # 방향 전환 다 하고 나서는 무한히 전진

t = 0
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
snake = [0, deque([(0, 0)])]  # 머리 방향, 뱀 리스트
for next_t, next_d in paths:
    game_over = False
    head_d = directions[snake[0]]
    while next_t > t:
        t += 1

        cur_head = snake[1][0]
        next_head = (cur_head[0] + head_d[0], cur_head[1] + head_d[1])
        # 벽에 부딪침
        if next_head[0] < 0 or next_head[0] >= N or next_head[1] < 0 or next_head[1] >= N:
            game_over = True
            break
        # 자기 몸에 부딪침
        elif next_head in snake[1]:
            game_over = True
            break
        # 사과에 부딪침
        elif board[next_head[0]][next_head[1]] == 1:
            snake[1].appendleft(next_head)
            board[next_head[0]][next_head[1]] = 0  # 먹은 사과는 사라짐... 이걸 못해서 틀림
        # 아무일 없음
        else:
            snake[1].pop()
            snake[1].appendleft(next_head)
    if game_over:
        break
    if next_d == 'L':
        snake[0] = (snake[0] + 1) % 4
    elif next_d == 'D':
        snake[0] = (snake[0] + 3) % 4
print(t)
