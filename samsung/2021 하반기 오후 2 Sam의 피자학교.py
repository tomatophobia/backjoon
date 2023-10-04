import sys

sys.stdin = open('input.txt', 'r')

import math


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def get_lo_hi(ll):
    lo = float('inf')
    hi = 0
    for elem in ll:
        if elem > hi:
            hi = elem
        if elem < lo:
            lo = elem
    return lo, hi


four = [[0, -1], [-1, 0], [0, 1], [1, 0]]
N, K = map(int, input().rstrip().split(' '))
dough = list(map(int, input().rstrip().split(' ')))

count = 0
while True:
    # 고저차 확인
    lo, hi = get_lo_hi(dough)
    if hi - lo <= K:
        break
    # 밀가루 작은 곳에 한 스푼
    for dd in range(N):
        if dough[dd] == lo:
            dough[dd] += 1
    # 도우 말기
    bottom = math.floor(math.sqrt(N))
    if bottom ** 2 <= N < bottom ** 2 + bottom:
        left = N - bottom ** 2
        board = [[0] * (bottom + left) for _ in range(bottom + left)]
        # 꼬다리
        j = 0
        for i in range(N - 1, N - 1 - left, -1):
            board[-1][-1 - j] = dough[i]
            j += 1
        # 나머지
        start = [left + bottom - 1, bottom - 1, 0]
        for i in range(N - 1 - left, -1, -1):
            x, y, d = start
            board[x][y] = dough[i]
            nx, ny = x + four[d][0], y + four[d][1]
            if not (left <= nx < bottom + left and 0 <= ny < bottom and board[nx][ny] == 0):
                d = (d + 1) % 4
                nx, ny = x + four[d][0], y + four[d][1]
            start = [nx, ny, d]
    else:
        left = N - (bottom ** 2 + bottom)
        board_len = max(bottom + left, bottom + 1)
        board = [[0] * board_len for _ in range(board_len)]
        # 꼬다리
        j = 0
        for i in range(N - 1, N - 1 - left - bottom, -1):
            board[-1][bottom + left - 1 - j] = dough[i]
            j += 1
        # 나머지
        start = [board_len - 2, 0, 1]
        for i in range(N - 1 - left - bottom, -1, -1):
            x, y, d = start
            board[x][y] = dough[i]
            nx, ny = x + four[d][0], y + four[d][1]
            if not (board_len - bottom - 1 <= nx < board_len - 1 and 0 <= ny < bottom and board[nx][ny] == 0):
                d = (d + 1) % 4
                nx, ny = x + four[d][0], y + four[d][1]
            start = [nx, ny, d]
    # 도우 누르기
    board_len = len(board)
    next_board = [board[i][:] for i in range(board_len)]
    for r in range(board_len):
        for c in range(board_len):
            if board[r][c] == 0:
                continue
            # 오른쪽, 아래
            for dr, dc in [[0, 1], [1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < board_len and 0 <= nc < board_len and board[nr][nc] > 0:
                    diff = abs(board[r][c] - board[nr][nc]) // 5
                    if board[r][c] > board[nr][nc]:
                        next_board[r][c] = next_board[r][c] - diff
                        next_board[nr][nc] = next_board[nr][nc] + diff
                    else:
                        next_board[r][c] = next_board[r][c] + diff
                        next_board[nr][nc] = next_board[nr][nc] - diff
    board = next_board
    next_dough = []
    for c in range(board_len):
        for r in range(board_len - 1, -1, -1):
            if board[r][c] > 0:
                next_dough.append(board[r][c])
    dough = next_dough
    # 도우 반 접기
    board_len = max(4, N // 4)
    board = [[0] * board_len for _ in range(board_len)]
    for i in range(0, N):
        if i < N // 4:
            k = i
            board[-2][-1 - k] = dough[i]
        elif i < N // 2:
            k = i - N // 4
            board[-3][- N // 4 + k] = dough[i]
        elif i < 3 * N // 4:
            k = i - N // 2
            board[-4][-1 - k] = dough[i]
        else:
            k = i - 3 * N // 4
            board[-1][- N // 4 + k] = dough[i]
    # 도우 누르기
    board_len = len(board)
    next_board = [board[i][:] for i in range(board_len)]
    for r in range(board_len):
        for c in range(board_len):
            if board[r][c] == 0:
                continue
            # 오른쪽, 아래
            for dr, dc in [[0, 1], [1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < board_len and 0 <= nc < board_len and board[nr][nc] > 0:
                    diff = abs(board[r][c] - board[nr][nc]) // 5
                    if board[r][c] > board[nr][nc]:
                        next_board[r][c] = next_board[r][c] - diff
                        next_board[nr][nc] = next_board[nr][nc] + diff
                    else:
                        next_board[r][c] = next_board[r][c] + diff
                        next_board[nr][nc] = next_board[nr][nc] - diff
    board = next_board
    next_dough = []
    for c in range(board_len):
        for r in range(board_len - 1, -1, -1):
            if board[r][c] > 0:
                next_dough.append(board[r][c])
    dough = next_dough
    # 카운트 증가
    count += 1
print(count)
