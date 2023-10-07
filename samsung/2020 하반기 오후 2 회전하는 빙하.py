import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f"{board[r][c]:4}", end='')
        print('')


four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().rstrip().split(' '))

board = []
LB = 2 ** N
for _ in range(LB):
    board.append(list(map(int, input().rstrip().split(' '))))
rotate = list(map(int, input().rstrip().split(' ')))
for q in range(Q):
    L = rotate[q]
    # 인접 회전
    if L > 0:
        for px in range(2 ** (N - L)):
            for py in range(2 ** (N - L)):
                temp1 = [[0] * 2 ** L for _ in range(2 ** L)]
                temp2 = [[0] * 2 ** L for _ in range(2 ** L)]
                # 평행이동 -> 회전 -> 평행이동
                for x in range(2 ** L):
                    for y in range(2 ** L):
                        temp1[x][y] = board[x + px * 2 ** L][y + py * 2 ** L]
                for x in range(2 ** (L - 1)):
                    for y in range(2 ** (L - 1)):
                        temp2[x][y + 2 ** (L - 1)] = temp1[x][y]
                for x in range(2 ** (L - 1)):
                    for y in range(2 ** (L - 1), 2 ** L):
                        temp2[x + 2 ** (L - 1)][y] = temp1[x][y]
                for x in range(2 ** (L - 1), 2 ** L):
                    for y in range(2 ** (L - 1)):
                        temp2[x - 2 ** (L - 1)][y] = temp1[x][y]
                for x in range(2 ** (L - 1), 2 ** L):
                    for y in range(2 ** (L - 1), 2 ** L):
                        temp2[x][y - 2 ** (L - 1)] = temp1[x][y]
                for x in range(2 ** L):
                    for y in range(2 ** L):
                        board[x + px * 2 ** L][y + py * 2 ** L] = temp2[x][y]
    # 녹음
    next_board = [board[i][:] for i in range(LB)]
    for x in range(LB):
        for y in range(LB):
            if board[x][y] == 0:
                continue
            count = 0
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, LB) and board[nx][ny] > 0:
                    count += 1
            if count < 3:
                if next_board[x][y] > 0:
                    next_board[x][y] -= 1
    board = next_board
# 전체 빙하 양
total = sum([sum(board[i]) for i in range(LB)])
print(total)
# 가장 큰 빙하 군집 BFS
visited = [[False] * LB for _ in range(LB)]
max_size = 0
for x in range(LB):
    for y in range(LB):
        if board[x][y] == 0:
            continue
        queue = deque([[x, y]])
        visited[x][y] = True
        size = 1
        while len(queue) > 0:
            cx, cy = queue.popleft()
            for dx, dy in four:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, LB) and not visited[nx][ny] and board[nx][ny] > 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    size += 1
        if size > max_size:
            max_size = size
print(max_size)
