import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def print_board(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(f"{board[x][y]:4}", end='')
        print('')


four = [[0, 1], [-1, 0], [0, -1], [1, 0]]
N, M = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))

# 점수판 미리 구하기
score_board = [[0] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if score_board[x][y] != 0:
            continue
        queue = deque([[x, y]])
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        target = [[x, y]]
        while len(queue):
            cx, cy = queue.popleft()
            for dx, dy in four:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    target.append([nx, ny])
        for tx, ty in target:
            score_board[tx][ty] = len(target) * board[x][y]

dice = [[[0] * 3 for _ in range(3)] for _ in range(3)]
dice[0][0][1] = 1
dice[0][-1][0] = 2
dice[1][0][0] = 3
dice[-1][0][0] = 4
dice[0][1][0] = 5
dice[0][0][-1] = 6
dice_pos = [0, 0]
dice_dir = 0

total = 0
for _ in range(M):
    # 움직임
    dx, dy = dice_pos
    nx, ny = dx + four[dice_dir][0], dy + four[dice_dir][1]
    if not is_valid(nx, ny, N):
        dice_dir = (dice_dir + 2) % 4
        nx, ny = dx + four[dice_dir][0], dy + four[dice_dir][1]
    dice_pos = [nx, ny]
    if dice_dir == 0:
        dice[1][0][0], dice[0][0][1] = dice[0][0][1], dice[1][0][0]
        dice[0][0][1], dice[-1][0][0] = dice[-1][0][0], dice[0][0][1]
        dice[-1][0][0], dice[0][0][-1] = dice[0][0][-1], dice[-1][0][0]
    elif dice_dir == 1:
        dice[0][1][0], dice[0][0][1] = dice[0][0][1], dice[0][1][0]
        dice[0][0][1], dice[0][-1][0] = dice[0][-1][0], dice[0][0][1]
        dice[0][-1][0], dice[0][0][-1] = dice[0][0][-1], dice[0][-1][0]
    elif dice_dir == 2:
        dice[-1][0][0], dice[0][0][1] = dice[0][0][1], dice[-1][0][0]
        dice[0][0][1], dice[1][0][0] = dice[1][0][0], dice[0][0][1]
        dice[1][0][0], dice[0][0][-1] = dice[0][0][-1], dice[1][0][0]
    if dice_dir == 3:
        dice[0][-1][0], dice[0][0][1] = dice[0][0][1], dice[0][-1][0]
        dice[0][0][1], dice[0][1][0] = dice[0][1][0], dice[0][0][1]
        dice[0][1][0], dice[0][0][-1] = dice[0][0][-1], dice[0][1][0]
    # 점수 계산 (BFS)
    dx, dy = dice_pos
    total += score_board[dx][dy]
    # 방향 전환
    if dice[0][0][-1] > board[dx][dy]:
        dice_dir = (dice_dir - 1) % 4
    elif dice[0][0][-1] < board[dx][dy]:
        dice_dir = (dice_dir + 1) % 4
print(total)
