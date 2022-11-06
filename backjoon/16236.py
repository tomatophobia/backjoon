import sys
from collections import deque


def pprint(board, shark, eat, count):
    print('========')
    print(shark, eat, count)
    for i in range(len(board)):
        for j in range(len(board)):
            if (i, j) == (shark[0], shark[1]):
                print('s', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


input = sys.stdin.readline

N = int(input())

shark = None
board = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    if 9 in line:
        j = line.index(9)
        shark = i, j, 2
        line[j] = 0
    board.append(line)

count = 0
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
eat = 0
while True:
    s = shark[0], shark[1]
    age = shark[2]
    queue = deque([(s, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[s[0]][s[1]] = True
    find = (shark[0], shark[1], float('inf'))
    while len(queue) > 0:
        cur, move = queue.popleft()
        if move >= find[2]:
            continue
        x, y = cur
        for d in directions:
            dx = x + d[0]
            dy = y + d[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N or visited[dx][dy] or board[dx][dy] > age:
                continue
            visited[dx][dy] = True
            if board[dx][dy] == age or board[dx][dy] == 0:
                queue.append(((dx, dy), move + 1))
            elif 0 < board[dx][dy] < age:
                fx, fy, fd = find
                if move + 1 < fd:
                    find = dx, dy, move + 1
                elif move + 1 == fd:
                    if dx < fx:
                        find = dx, dy, move + 1
                    elif dx == fx and dy < fy:
                        find = dx, dy, move + 1
    if find[2] == float('inf'):
        break
    fx, fy, fd = find
    eat += 1
    count += fd
    board[fx][fy] = 0
    if eat == age:
        eat = 0
        shark = (fx, fy, age + 1)
    else:
        shark = (fx, fy, age)

print(count)
