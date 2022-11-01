import sys


def pprint(board):
    print('========')
    for l in board:
        for e in l:
            print(e, end=' ')
        print()


def to_radix_d(n, d, l):
    result = []
    while (True):
        q, r = divmod(n, d)
        result.append(r)
        if q == 0:
            break
        n = q
    while len(result) < l:
        result.append(0)
    return result


input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = []
cc = [[], [], [], [], []]
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    for j in range(M):
        if 0 < line[j] < 6:
            cc[line[j] - 1].append((i, j))
    board.append(line)

for x, y in cc[4]:
    down = x + 1
    while down < N and board[down][y] != 6:
        if board[down][y] == 0:
            board[down][y] = '#'
        down += 1
    up = x - 1
    while up >= 0 and board[up][y] != 6:
        if board[up][y] == 0:
            board[up][y] = '#'
        up -= 1
    right = y + 1
    while right < M and board[x][right] != 6:
        if board[x][right] == 0:
            board[x][right] = '#'
        right += 1
    left = y - 1
    while left >= 0 and board[x][left] != 6:
        if board[x][left] == 0:
            board[x][left] = '#'
        left -= 1

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min_count = float('inf')
for i in range(pow(4, len(cc[0]))):
    c1 = to_radix_d(i, 4, len(cc[0]))
    for j in range(pow(2, len(cc[1]))):
        c2 = to_radix_d(j, 2, len(cc[1]))
        for k in range(pow(4, len(cc[2]))):
            c3 = to_radix_d(k, 4, len(cc[2]))
            for l in range(pow(4, len(cc[3]))):
                c4 = to_radix_d(l, 4, len(cc[3]))
                copy_board = [line[:] for line in board]
                for c in range(len(cc[0])):
                    x, y = cc[0][c]
                    dx, dy = directions[c1[c]]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                for c in range(len(cc[1])):
                    x, y = cc[1][c]
                    dx, dy = directions[c2[c]]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                    x, y = cc[1][c]
                    dx, dy = directions[(c2[c] + 2) % 4]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                for c in range(len(cc[2])):
                    x, y = cc[2][c]
                    dx, dy = directions[c3[c]]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                    x, y = cc[2][c]
                    dx, dy = directions[(c3[c] + 1) % 4]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy

                for c in range(len(cc[3])):
                    x, y = cc[3][c]
                    dx, dy = directions[c4[c]]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                    x, y = cc[3][c]
                    dx, dy = directions[(c4[c] + 1) % 4]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy
                    x, y = cc[3][c]
                    dx, dy = directions[(c4[c] + 2) % 4]
                    x += dx
                    y += dy
                    while 0 <= x < N and 0 <= y < M and copy_board[x][y] != 6:
                        if copy_board[x][y] == 0:
                            copy_board[x][y] = '#'
                        x += dx
                        y += dy

                cur_count = 0
                for row in range(N):
                    for col in range(M):
                        if copy_board[row][col] == 0:
                            cur_count += 1
                if cur_count < min_count:
                    min_count = cur_count
print(min_count)
