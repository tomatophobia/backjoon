import sys


def copy_2d(origin):
    return [origin[i][:] for i in range(len(origin))]


input = sys.stdin.readline

fishes = [[[0, 0], 0]] * 16  # 번호 -> 위치, 방향
board = [[[0, 0]] * 4 for _ in range(4)]  # 위치 -> 번호, 방향

dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in range(4):
    l = list(map(int, input().rstrip().split(' ')))
    for j in range(4):
        n, d = l[2 * j] - 1, l[2 * j + 1] - 1
        fishes[n] = [[i, j], d]
        board[i][j] = [n, d]

# DFS
stack = []
shark = [[0, 0], board[0][0][1], board[0][0][0] + 1]  # 위치, 방향, 점수
fishes[board[0][0][0]] = None
board[0][0] = None
stack.append([shark, fishes[:], copy_2d(board), [[0, 0]]])

max_score = 0
while len(stack) > 0:
    shark, fishes, board, trace = stack.pop()
    [x, y], d, score = shark

    # 물고기 이동
    for i in range(len(fishes)):
        if fishes[i] is not None:
            [fx, fy], fd = fishes[i]
            c = 0
            while c < 8:
                dfx, dfy = fx + dirs[(fd + c) % 8][0], fy + dirs[(fd + c) % 8][1]
                if 0 <= dfx < 4 and 0 <= dfy < 4 and (dfx, dfy) != (x, y):
                    break
                c += 1
            if c == 8:
                continue
            fd = (fd + c) % 8
            if board[dfx][dfy] is None:
                fishes[i] = [[dfx, dfy], fd]
                board[fx][fy] = None
                board[dfx][dfy] = [i, fd]
            else:
                tn, td = board[dfx][dfy]
                fishes[i] = [[dfx, dfy], fd]
                fishes[tn] = [[fx, fy], td]
                board[fx][fy] = [tn, td]
                board[dfx][dfy] = [i, fd]

    # 상어 이동
    end = True
    for i in range(1, 4):
        dx, dy = x + dirs[d][0] * i, y + dirs[d][1] * i
        if dx < 0 or dx >= 4 or dy < 0 or dy >= 4 or board[dx][dy] is None:
            continue
        end = False
        fn, fd = board[dx][dy]
        next_fishes = fishes[:]
        next_board = copy_2d(board)
        next_fishes[fn] = None
        next_board[dx][dy] = None
        next_shark = [[dx, dy], fd, score + fn + 1]
        stack.append([next_shark, next_fishes, next_board, trace[:] + [[dx, dy]]])
    if end:
        if score > max_score:
            max_score = score
print(max_score)
