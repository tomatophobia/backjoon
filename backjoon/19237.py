import sys

input = sys.stdin.readline

N, M, k = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(lambda s: [int(s) - 1] if s != '0' else None, input().rstrip().split(' ')))
    board.append(line)
# 상어 => [번호], 냄새 => [번호, 지속 시간]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

shark_dirs = list(map(lambda s: int(s) - 1, input().rstrip().split(' ')))
shark_table = []
for _ in range(M):
    t = []
    for j in range(4):
        line = list(map(lambda s: int(s) - 1, input().rstrip().split(' ')))
        t.append(line)
    shark_table.append(t)

t = 0
left = M - 1
while t <= 1000 and left > 0:
    # 상어 이동
    next_board = [[None] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            e = board[x][y]
            if e is not None and len(e) == 1:
                shark_num = e[0]
                shark_dir = shark_dirs[shark_num]
                found = False
                dx, dy = 0, 0
                for next_dir in shark_table[shark_num][shark_dir]:
                    dx, dy = x + dirs[next_dir][0], y + dirs[next_dir][1]
                    if 0 <= dx < N and 0 <= dy < N and board[dx][dy] is None:
                        found = True
                        break
                if not found:
                    for next_dir in shark_table[shark_num][shark_dir]:
                        dx, dy = x + dirs[next_dir][0], y + dirs[next_dir][1]
                        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] is not None and board[dx][dy][0] == shark_num:
                            break
                shark_dirs[shark_num] = next_dir
                if k - 1 > 0:
                    next_board[x][y] = [shark_num, k - 1]
                already = next_board[dx][dy]
                if already is None:
                    next_board[dx][dy] = [shark_num]
                else:
                    next_board[dx][dy] = [shark_num if shark_num <= already[0] else already[0]]
                    left -= 1
    # 냄새 감소
    for x in range(N):
        for y in range(N):
            e = board[x][y]
            if e is not None and len(e) == 2:
                if next_board[x][y] is None:
                    if e[1] - 1 > 0:
                        next_board[x][y] = [e[0], e[1] - 1]
    board = next_board
    t += 1

if t > 1000:
    print(-1)
else:
    print(t)
