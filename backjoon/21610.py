import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

moves = []
for _ in range(M):
    d, s = map(int, input().rstrip().split(' '))
    d -= 1
    moves.append([d, s])

dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cross = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
clouds = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
for d, s in moves:
    waters = []
    for x, y in clouds:
        dx, dy = (x + dirs[d][0] * s) % N, (y + dirs[d][1] * s) % N
        board[dx][dy] += 1
        waters.append([dx, dy])
    counts = []
    for x, y in waters:
        count = 0
        for c in cross:
            dx, dy = x + c[0], y + c[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N or board[dx][dy] <= 0:
                continue
            count += 1
        counts.append(count)
    check = [[False] * N for _ in range(N)]
    for i in range(len(waters)):
        x, y = waters[i]
        if counts[i] > 0:
            board[x][y] += counts[i]
        check[x][y] = True
    clouds = []
    for x in range(N):
        for y in range(N):
            if board[x][y] < 2 or check[x][y]:
                continue
            board[x][y] -= 2
            clouds.append([x, y])
count = 0
for x in range(N):
    for y in range(N):
        count += board[x][y]
print(count)
