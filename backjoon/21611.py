import sys


def snake_to_list(x, y, N):
    if x == N // 2 and y == N // 2:
        return 0
    k = N // 2
    d = max(abs(x - k), abs(y - k))
    if x - k == -d:
        return 4 * d * (d + 1) - y + k - d
    elif y - k == d:
        return 4 * d * (d + 1) - 2 * d - x + k - d
    elif x - k == d:
        return 4 * d * (d + 1) - 4 * d - k - d + y
    else:
        return 4 * d * (d + 1) - 6 * d - k - d + x

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

line = [0] * (N * N)
for r in range(N):
    for c in range(N):
        line[snake_to_list(r, c, N)] = board[r][c]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
score = 0
for _ in range(M):
    d, s = map(int, input().rstrip().split(' '))
    d -= 1
    cx, cy = N // 2, N // 2
    for si in range(1, s + 1):
        dx, dy = cx + dirs[d][0] * si, cy + dirs[d][1] * si
        target = snake_to_list(dx, dy, N)
        line[target] = 0
    new_line = [0] * (N * N)
    c = 1
    for i in range(1, N * N):
        if line[i] != 0:
            new_line[c] = line[i]
            c += 1
    line = new_line

    while True:
        bomb = False
        cur = 0
        count = 0
        for i in range(1, N * N):
            if cur == line[i]:
                count += 1
            else:
                if count >= 4:
                    bomb = True
                    score += cur * count
                    for j in range(1, count + 1):
                        line[i-j] = 0
                if line[i] == 0:
                    break
                cur = line[i]
                count = 1
        if not bomb:
            break
        new_line = [0] * (N * N)
        c = 1
        for i in range(1, N * N):
            if line[i] != 0:
                new_line[c] = line[i]
                c += 1
        line = new_line

    new_line = [0]
    cur = 0
    count = 0
    for i in range(1, N * N):
        if cur == line[i]:
            count += 1
        else:
            if cur != 0:
                new_line.append(count)
                new_line.append(cur)
            if line[i] == 0 or len(new_line) > N * N:
                break
            cur = line[i]
            count = 1
    if len(new_line) < N * N:
        new_line.extend([0] * (N * N - len(new_line)))
    else:
        new_line = new_line[:N*N]
    line = new_line
print(score)
