import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

dice = [[[0] * 3 for _ in range(3)] for _ in range(3)]
dice[1][0][0] = 3
dice[0][1][0] = 2
dice[-1][0][0] = 4
dice[0][-1][0] = 5
dice[0][0][1] = 1
dice[0][0][-1] = 6
pos = [0, 0]
dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
way = 0  # right 0, up 1, left 2, down 3
score = 0
for _ in range(K):
    # move
    x, y = pos
    dx, dy = x + dirs[way][0], y + dirs[way][1]
    if dx < 0 or dx >= N or dy < 0 or dy >= M:
        way = (way + 2) % 4
        dx, dy = x + dirs[way][0], y + dirs[way][1]
    pos = dx, dy
    x, y = pos
    if way == 0:
        for i in range(3):
            x1, z1 = dirs[i]
            x2, z2 = dirs[(i + 1) % 4]
            dice[x1][0][z1], dice[x2][0][z2] = dice[x2][0][z2], dice[x1][0][z1]
    elif way == 1:
        for i in range(3):
            y1, z1 = dirs[i]
            y2, z2 = dirs[(i + 1) % 4]
            dice[0][y1][z1], dice[0][y2][z2] = dice[0][y2][z2], dice[0][y1][z1]
    elif way == 2:
        for i in range(3, 0, -1):
            x1, z1 = dirs[i]
            x2, z2 = dirs[(i + 1) % 4]
            dice[x1][0][z1], dice[x2][0][z2] = dice[x2][0][z2], dice[x1][0][z1]
    elif way == 3:
        for i in range(3, 0, -1):
            y1, z1 = dirs[i]
            y2, z2 = dirs[(i + 1) % 4]
            dice[0][y1][z1], dice[0][y2][z2] = dice[0][y2][z2], dice[0][y1][z1]
    A = dice[0][0][-1]
    B = board[x][y]
    # score
    C = 1
    queue = deque()
    queue.append([x, y])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while len(queue) > 0:
        a, b = queue.popleft()
        for d in dirs:
            da, db = a + d[0], b + d[1]
            if da < 0 or da >= N or db < 0 or db >= M or visited[da][db] or board[da][db] != B:
                continue
            queue.append([da, db])
            visited[da][db] = True
            C += 1
    score += B * C
    # turn
    if A > B:
        way = (way - 1) % 4
    elif A < B:
        way = (way + 1) % 4
print(score)
