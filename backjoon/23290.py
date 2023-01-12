import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M, S = map(int, input().rstrip().split(' '))

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs_four = [[-1, 0], [0, -1], [1, 0], [0, 1]]
board = [[[0, 0] for _ in range(4)] for _ in range(4)]  # [shark, smell]

fishes = []
for _ in range(M):
    x, y, d = map(lambda s: int(s) - 1, input().rstrip().split(' '))
    fishes.append([[x, y], d])

sx, sy = map(lambda s: int(s) - 1, input().rstrip().split(' '))
shark = [sx, sy]

board[sx][sy][0] = 1

for _ in range(S):
    # copy fish
    copied = fishes[:]
    # move fish
    next_fishes = []
    for [x, y], d in fishes:
        dd = d
        dx, dy = x + dirs[dd][0], y + dirs[dd][1]
        tryCount = 0
        while (dx < 0 or dx >= 4 or dy < 0 or dy >= 4 or board[dx][dy] != [0, 0]) and tryCount < 8:
            dd = (dd - 1) % 8
            dx, dy = x + dirs[dd][0], y + dirs[dd][1]
            tryCount += 1
        if tryCount == 8:
            next_fishes.append([[x, y], d])
        else:
            next_fishes.append([[dx, dy], dd])
    fishes = next_fishes
    # move shark
    max_move = [4, 4, 4]
    max_eat = -1
    x, y = shark
    for i in range(4):
        dx1, dy1 = x + dirs_four[i][0], y + dirs_four[i][1]
        if dx1 < 0 or dx1 >= 4 or dy1 < 0 or dy1 >= 4:
            continue
        for j in range(4):
            dx2, dy2 = dx1 + dirs_four[j][0], dy1 + dirs_four[j][1]
            if dx2 < 0 or dx2 >= 4 or dy2 < 0 or dy2 >= 4:
                continue
            for k in range(4):
                dx3, dy3 = dx2 + dirs_four[k][0], dy2 + dirs_four[k][1]
                if dx3 < 0 or dx3 >= 4 or dy3 < 0 or dy3 >= 4:
                    continue
                eat = 0
                for fpos, _ in fishes:
                    if [dx1, dy1] == fpos or [dx2, dy2] == fpos or [dx3, dy3] == fpos:
                        eat += 1
                if eat > max_eat:
                    max_eat = eat
                    max_move = [i, j, k]
    i, j, k = max_move
    dx1, dy1 = x + dirs_four[i][0], y + dirs_four[i][1]
    dx2, dy2 = dx1 + dirs_four[j][0], dy1 + dirs_four[j][1]
    dx3, dy3 = dx2 + dirs_four[k][0], dy2 + dirs_four[k][1]
    new_fishes = []
    for [fx, fy], d in fishes:
        if [fx, fy] == [dx1, dy1]:
            board[fx][fy][1] = 3
        elif [fx, fy] == [dx2, dy2]:
            board[fx][fy][1] = 3
        elif [fx, fy] == [dx3, dy3]:
            board[fx][fy][1] = 3
        else:
            new_fishes.append([[fx, fy], d])
    fishes = new_fishes
    board[x][y][0] = 0
    board[dx3][dy3][0] = 1
    shark = [dx3, dy3]
    # remove smell
    for r in range(4):
        for c in range(4):
            if board[r][c][1] > 0:
                board[r][c][1] -= 1
    # copy fish
    fishes.extend(copied)
print(len(fishes))
