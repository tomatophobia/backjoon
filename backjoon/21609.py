import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

origin = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    origin.append(line)

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
score = 0
while True:
    # remove the largest block group
    board = [origin[i][:] for i in range(N)]
    max_group = None
    max_rainbow = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] is None or board[x][y] <= 0:
                continue
            color = board[x][y]
            board[x][y] = -1
            queue = deque()
            queue.append([x, y])
            visited = [[False] * N for _ in range(N)]
            visited[x][y] = True
            group = [[x, y]]
            rainbow = 0
            while len(queue) > 0:
                r, c = queue.popleft()
                for d in dirs:
                    dr, dc = r + d[0], c + d[1]
                    if dr < 0 or dr >= N or dc < 0 or dc >= N or board[dr][dc] is None or visited[dr][dc]:
                        continue
                    if board[dr][dc] == -1 or (board[dr][dc] != 0 and board[dr][dc] != color):
                        continue
                    if board[dr][dc] == 0:
                        rainbow += 1
                    else:
                        board[dr][dc] = -1
                    queue.append([dr, dc])
                    visited[dr][dc] = True
                    group.append([dr, dc])
            if max_group is None:
                max_group = group
                max_rainbow = rainbow
            elif len(max_group) < len(group):
                max_group = group
                max_rainbow = rainbow
            elif len(max_group) == len(group) and max_rainbow < rainbow:
                max_group = group
                max_rainbow = rainbow
            elif len(max_group) == len(group) and max_rainbow == rainbow:
                max_group = group
                max_rainbow = rainbow
    if max_group is None or len(max_group) == 1:
        break
    for r, c in max_group:
        origin[r][c] = None
    score += len(max_group) ** 2
    # gravity
    for r in range(N - 2, -1, -1):
        for c in range(N):
            if origin[r][c] is None or origin[r][c] == -1:
                continue
            dr = r
            while dr + 1 < N and origin[dr + 1][c] is None:
                origin[dr + 1][c] = origin[dr][c]
                origin[dr][c] = None
                dr += 1
    # rotate counter clockwise
    new_origin = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_origin[-c + N - 1][r] = origin[r][c]
    origin = new_origin
    # gravity
    for r in range(N - 2, -1, -1):
        for c in range(N):
            if origin[r][c] is None or origin[r][c] == -1:
                continue
            dr = r
            while dr + 1 < N and origin[dr + 1][c] is None:
                origin[dr + 1][c] = origin[dr][c]
                origin[dr][c] = None
                dr += 1
print(score)
