import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().rstrip().split(' '))

board = []
for _ in range(2 ** N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

L = list(map(int, input().rstrip().split(' ')))

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for q in range(Q):
    # storm
    new_board = [[None] * 2 ** N for _ in range(2 ** N)]
    l = L[q]
    for i in range(2 ** (N - l)):
        for j in range(2 ** (N - l)):
            k = 2 ** l
            x, y = i * k, j * k
            for p in range(x, x + k):
                for q in range(y, y + k):
                    new_board[p][q] = board[-q + y + k - 1 + x][p - x + y]
    board = new_board

    # fire
    melt = []
    for r in range(2 ** N):
        for c in range(2 ** N):
            count = 0
            for d in dirs:
                dr, dc = r + d[0], c + d[1]
                if dr < 0 or dr >= 2 ** N or dc < 0 or dc >= 2 ** N or board[dr][dc] <= 0:
                    continue
                count += 1
            if count < 3 and board[r][c] > 0:
                melt.append([r, c])
    for r, c in melt:
        board[r][c] -= 1

ice = 0
for r in range(2 ** N):
    for c in range(2 ** N):
        ice += board[r][c]
print(ice)

visited = [[False] * 2 ** N for _ in range(2 ** N)]
max_count = 0
for r in range(2 ** N):
    for c in range(2 ** N):
        if visited[r][c] or board[r][c] <= 0:
            continue
        queue = deque()
        queue.append([r, c])
        visited[r][c] = True
        count = 1
        while len(queue) > 0:
            r, c = queue.popleft()
            for d in dirs:
                dr, dc = r + d[0], c + d[1]
                if dr < 0 or dr >= 2 ** N or dc < 0 or dc >= 2 ** N or visited[dr][dc] or board[dr][dc] <= 0:
                    continue
                queue.append([dr, dc])
                visited[dr][dc] = True
                count += 1
        if count > max_count:
            max_count = count
print(max_count)
