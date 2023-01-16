import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, D = map(int, input().rstrip().split(' '))
origin = []
enemy_count = 0
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    enemy_count += line.count(1)
    origin.append(line)

dirs = [[0, -1], [-1, 0], [0, 1]]
max_kill = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            board = [origin[i][:] for i in range(N)]
            left = enemy_count
            kill_count = 0
            while left > 0:
                to_die = []
                for c in [i, j, k]:
                    x, y = N - 1, c
                    if board[x][y] == 1:
                        to_die.append([x, y])
                    else:
                        visited = [[False] * M for _ in range(N)]
                        visited[x][y] = True
                        queue = deque()
                        queue.append([x, y, 1])
                        while len(queue) > 0:
                            x, y, dist = queue.popleft()
                            if dist >= D:
                                continue
                            found = False
                            for d in dirs:
                                dx, dy = x + d[0], y + d[1]
                                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                                    continue
                                if board[dx][dy] == 1:
                                    found = True
                                    to_die.append([dx, dy])
                                    break
                                visited[dx][dy] = True
                                queue.append([dx, dy, dist + 1])
                            if found:
                                break
                for x, y in to_die:
                    if board[x][y] == 1:
                        board[x][y] = 0
                        kill_count += 1
                        left -= 1
                for e in board[N-1]:
                    if e == 1:
                        left -= 1
                board.pop()
                board.insert(0, [0] * M)
            if kill_count > max_kill:
                max_kill = kill_count
print(max_kill)
