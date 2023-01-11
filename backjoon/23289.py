import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C, K = map(int, input().rstrip().split(' '))
board = []
air = []
investigate = []
for i in range(R):
    line = list(map(int, input().rstrip().split(' ')))
    for j in range(C):
        if 0 < line[j] < 5:
            air.append([[i, j], line[j] - 1])
        elif line[j] == 5:
            investigate.append([i, j])
        else:
            continue
        line[j] = 0
    board.append(line)
W = int(input())
walls = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(W):
    x, y, t = map(int, input().rstrip().split(' '))
    x -= 1
    y -= 1
    if t == 0:
        walls[x][y].append([x - 1, y])
    else:
        walls[x][y].append([x, y + 1])

dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
hot = []
for x, y in dirs:
    temp = []
    for i in range(5):
        sx, sy = (i + 1) * x - i * y, (i + 1) * y + i * x
        for j in range(2 * i + 1):
            dx, dy = sx + j * y, sy - j * x
            temp.append([dx, dy, 5 - i])
    hot.append(temp)
count = 0
while count <= 100:
    for [r, c], d in air:
        hotted = [[False] * C for _ in range(R)]
        dx, dy = dirs[d][0], dirs[d][1]
        sr, sc = r + dx, c + dy
        hotted[sr][sc] = True
        queue = [[sr, sc]]
        board[sr][sc] += 5
        for i in range(4):
            temp = []
            for x, y in queue:
                # 1
                if x - dy < 0 or x - dy >= R or y + dx < 0 or y + dx >= C or x + dx - dy < 0 or x + dx - dy >= R or y + dx + dy < 0 or y + dx + dy >= C or hotted[x + dx - dy][y + dx + dy]:
                    pass
                elif [x - dy, y + dx] in walls[x][y] or [x, y] in walls[x - dy][y + dx]:
                    pass
                elif [x + dx - dy, y + dx + dy] in walls[x - dy][y + dx] or [x - dy, y + dx] in walls[x + dx - dy][y + dx + dy]:
                    pass
                else:
                    hotted[x + dx - dy][y + dx + dy] = True
                    temp.append([x + dx - dy, y + dx + dy])
                    board[x + dx - dy][y + dx + dy] += 4 - i
                # 2
                if x + dx < 0 or x + dx >= R or y + dy < 0 or y + dy >= C or hotted[x + dx][y + dy]:
                    pass
                elif [x + dx, y + dy] in walls[x][y] or [x, y] in walls[x + dx][y + dy]:
                    pass
                else:
                    hotted[x + dx][y + dy] = True
                    temp.append([x + dx, y + dy])
                    board[x + dx][y + dy] += 4 - i
                # 3
                if x + dy < 0 or x + dy >= R or y - dx < 0 or y - dx >= C or x + dx + dy < 0 or x + dx + dy >= R or y - dx + dy < 0 or y - dx + dy >= C or hotted[x + dx + dy][y - dx + dy]:
                    pass
                elif [x + dy, y - dx] in walls[x][y] or [x, y] in walls[x + dy][y - dx]:
                    pass
                elif [x + dx + dy, y - dx + dy] in walls[x + dy][y - dx] or [x + dy, y - dx] in walls[x + dx + dy][y - dx + dy]:
                    pass
                else:
                    hotted[x + dx + dy][y - dx + dy] = True
                    temp.append([x + dx + dy, y - dx + dy])
                    board[x + dx + dy][y - dx + dy] += 4 - i
            queue = temp
    new_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            ct = board[r][c]
            for d in dirs:
                dr, dc = r + d[0], c + d[1]
                if dr < 0 or dr >= R or dc < 0 or dc >= C or board[r][c] <= board[dr][dc]:
                    continue
                elif [dr, dc] in walls[r][c] or [r, c] in walls[dr][dc]:
                    continue
                m = (board[r][c] - board[dr][dc]) // 4
                ct -= m
                new_board[dr][dc] += m
            new_board[r][c] += ct
    board = new_board
    for r in [0, R - 1]:
        for c in range(C):
            if board[r][c] > 0:
                board[r][c] -= 1
    for r in range(1, R-1):
        for c in [0, C - 1]:
            if board[r][c] > 0:
                board[r][c] -= 1
    count += 1
    end = True
    for r, c in investigate:
        if board[r][c] < K:
            end = False
            break
    if end:
        break
print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))
if count > 100:
    print(101)
else:
    print(count)
