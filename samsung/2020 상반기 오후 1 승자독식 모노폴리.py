import sys

sys.stdin = open('input.txt', 'r')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f"{board[r][c]:4}", end='')
        print('')


four = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M, K = map(int, input().rstrip().split(' '))
board = [[[] for _ in range(N)] for _ in range(N)]
pos = [[] for _ in range(M)]
move_priority = [[] for _ in range(M)]
for x in range(N):
    ll = list(map(int, input().rstrip().split(' ')))
    for y in range(N):
        if ll[y] > 0:
            pos[ll[y] - 1] = [x, y]
            board[x][y] = [ll[y] - 1, K]
dlist = list(map(int, input().rstrip().split(' ')))
for i in range(M):
    pos[i].append(dlist[i] - 1)
for i in range(M):
    for _ in range(4):
        move_priority[i].append(list(map(lambda x: int(x) - 1, input().rstrip().split(' '))))

count = 0
while count <= 1000:
    count += 1
    # 이동
    duplicate = [[[] for _ in range(N)] for _ in range(N)]
    for pi in range(M):
        if len(pos[pi]) == 0:
            continue
        x, y, d = pos[pi]
        bx, by, bd = x, y, -1
        for dd in move_priority[pi][d]:
            nx, ny = x + four[dd][0], y + four[dd][1]
            if not is_valid(nx, ny, N):
                continue
            if len(board[nx][ny]) == 0:
                bx, by, bd = nx, ny, dd
                break
            elif bd == -1 and board[nx][ny][0] == pi:
                bx, by, bd = nx, ny, dd
        duplicate[bx][by].append([pi, bd])
    # 턴 줄이기
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) == 0:
                continue
            pi, k = board[x][y]
            if k - 1 == 0:
                board[x][y] = []
            else:
                board[x][y] = [pi, k - 1]
    # 경합
    next_pos = [[] for _ in range(M)]
    live = 0
    for x in range(N):
        for y in range(N):
            if len(duplicate[x][y]) == 0:
                continue
            pi, d = min(duplicate[x][y])
            next_pos[pi] = [x, y, d]
            board[x][y] = [pi, K]
            live += 1
    pos = next_pos
    if live == 1:
        break
if count > 1000:
    print(-1)
else:
    print(count)
