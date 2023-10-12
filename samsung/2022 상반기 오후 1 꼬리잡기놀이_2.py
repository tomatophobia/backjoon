import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


four = [[0, 1], [-1, 0], [0, -1], [1, 0]]
N, M, K = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
# 뱀 만들기
snakes = []  # [뱀 데크, 헤드 방향 True = 왼쪽]
for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            snake = deque([[x, y]])
            board[x][y] = 4
            # 몸통
            queue = deque([[x, y]])
            while len(queue) > 0:
                cx, cy = queue.popleft()
                for dx, dy in four:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny, N) and board[nx][ny] == 2:
                        queue.append([nx, ny])
                        snake.append([nx, ny])
                        board[nx][ny] = 4
            # 꼬리
            cx, cy = snake[-1]
            for dx, dy in four:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, N) and board[nx][ny] == 3:
                    snake.append([nx, ny])
                    board[nx][ny] = 4
            snakes.append([snake, True])
score = 0
for k in range(K):
    # 뱀 이동
    snake_board = [[-1] * N for _ in range(N)]  # 뱀 번호가 찍힌 보드 (공 던질 때 쓸 것)
    for si in range(M):
        snake, head = snakes[si]
        x, y = snake[0] if head else snake[-1]
        sx, sy = snake[1] if head else snake[-2]
        nx, ny = x, y
        for dx, dy in four:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, N) and board[nx][ny] == 4 and [nx, ny] != [sx, sy]:
                break
        if head:
            snake.pop()
            snake.appendleft([nx, ny])
        else:
            snake.popleft()
            snake.append([nx, ny])
        for x, y in snake:
            snake_board[x][y] = si
    # 공던지기
    # 시작 위치 선정
    bx, by, bd = -1, -1, -1
    kk = k % (4 * N)
    if 0 <= kk < N:
        bx, by, bd = kk, 0, 0
    elif N <= kk < 2 * N:
        bx, by, bd = N - 1, kk - N, 1
    elif 2 * N <= kk < 3 * N:
        bx, by, bd = N - 1 - kk + 2 * N, N - 1, 2
    else:
        bx, by, bd = 0, N - 1 - kk + 3 * N, 3
    # 공 움직임
    hit = -1
    hx, hy = -1, -1
    for i in range(N):
        bbx, bby = bx + four[bd][0] * i, by + four[bd][1] * i
        if snake_board[bbx][bby] >= 0:
            hit = snake_board[bbx][bby]
            hx, hy = bbx, bby
            break
    # 뱀 방향 바꾸기
    if hit >= 0:
        hit_snake, hit_head = snakes[hit]
        idx = 0
        for si in range(len(hit_snake)):
            if [hx, hy] == hit_snake[si]:
                if hit_head:
                    score += (si + 1) ** 2
                else:
                    score += (len(hit_snake) - si) ** 2
                break
        snakes[hit][1] = not snakes[hit][1]
print(score)
