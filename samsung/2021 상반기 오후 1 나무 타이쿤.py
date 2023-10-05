import sys

sys.stdin = open('input.txt', 'r')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


eight = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
N, M = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
drug = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for _ in range(M):
    # 움직임 입력
    d, p = map(int, input().rstrip().split(' '))
    d = d - 1
    # 1. 특수영양제 이동
    next_board = [board[i][:] for i in range(N)]
    next_drug = []
    for cx, cy in drug:
        nx, ny = (cx + eight[d][0] * p) % N, (cy + eight[d][1] * p) % N
        # 2. 특수 영양제 투입
        next_board[nx][ny] += 1
        next_drug.append([nx, ny])
    drug = next_drug
    board = next_board
    # 3. 대각선 나무 수만큼 성장
    next_board = [board[i][:] for i in range(N)]
    for nx, ny in drug:
        for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            px, py = nx + dx, ny + dy
            if is_valid(px, py, N) and board[px][py] > 0:
                next_board[nx][ny] += 1
    board = next_board
    # 4. 나무 자르고 새로운 영양제 위치
    next_drug = []
    for x in range(N):
        for y in range(N):
            if board[x][y] >= 2 and [x, y] not in drug:
                board[x][y] -= 2
                next_drug.append([x, y])
    drug = next_drug
count = sum([sum(board[i]) for i in range(N)])
print(count)
