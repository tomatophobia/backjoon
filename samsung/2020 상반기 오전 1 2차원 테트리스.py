import sys

sys.stdin = open('input.txt', 'r')


def print_board(board):
    print("---")
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f"{board[r][c]:4}", end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def calm_down(board, start):
    while True:
        next_start = []
        fail = False
        for x, y in start:
            nx, ny = x + 1, y
            if is_valid(nx, ny, len(board)) and not board[nx][ny]:
                next_start.append([nx, ny])
            else:
                fail = True
                break
        if fail:
            break
        start = next_start
    for x, y in start:
        board[x][y] = True
    return board


def remove_one_line(board):
    count = 0
    next_board = [board[0][:], board[1][:]]
    for r in range(2, len(board)):
        bomb = True
        for c in range(len(board[r])):
            if not board[r][c]:
                bomb = False
                break
        if bomb:
            count += 1
        else:
            next_board.append(board[r][:])
    for _ in range(count):
        next_board = [[False] * 4] + next_board
    return count, next_board


def remove_overflow(board):
    for _ in range(2):
        remove = False
        for c in range(4):
            if board[1][c]:
                remove = True
                break
        if remove:
            board.pop()
            board = [[False] * 4] + board
        else:
            break
    return board


types = [[], [[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]
down_board = [[False] * 4 for _ in range(6)]
right_board = [[False] * 4 for _ in range(6)]
score = 0
K = int(input())
for _ in range(K):
    t, x, y = map(int, input().rstrip().split(' '))
    # 시작 포지션 선정
    down_start = []
    right_start = []
    for tx, ty in types[t]:
        down_start.append([tx, y + ty])
        right_start.append([ty, 3 - x - tx])
    # 내려가기
    down_board = calm_down(down_board, down_start)
    right_board = calm_down(right_board, right_start)
    # 합쳐진 라인 삭제
    cc1, down_board = remove_one_line(down_board)
    cc2, right_board = remove_one_line(right_board)
    score += cc1 + cc2
    # 넘친 라인 삭제
    down_board = remove_overflow(down_board)
    right_board = remove_overflow(right_board)
print(score)
count = 0
for r in range(6):
    for c in range(4):
        if down_board[r][c]:
            count += 1
        if right_board[r][c]:
            count += 1
print(count)
