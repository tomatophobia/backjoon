import sys

sys.stdin = open('input.txt', 'r')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N = int(input().rstrip())
board = [[0] * N for _ in range(N)]
fr_map = []
for _ in range(N ** 2):
    nlist = list(map(int, input().rstrip().split(' ')))
    max_score = [-1, -1]
    max_pos = []
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                continue
            score = [0, 0]
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if not is_valid(nx, ny, N):
                    continue
                if board[nx][ny] in nlist[1:]:
                    score[0] += 1
                elif board[nx][ny] == 0:
                    score[1] += 1
            if score > max_score:
                max_score = score
                max_pos = [x, y]
    mx, my = max_pos
    board[mx][my] = nlist[0]
    fr_map.append([max_pos, nlist[1:]])
# 점수 계산
score = 0
for [[mx, my], nl] in fr_map:
    count = 0
    for dx, dy in four:
        nx, ny = mx + dx, my + dy
        if is_valid(nx, ny, N) and board[nx][ny] in nl:
            count += 1
    if count > 0:
        score += 10 ** (count - 1)
print(score)
