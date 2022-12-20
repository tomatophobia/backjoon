import sys
from collections import deque

input = sys.stdin.readline

N, M, L = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

car = list(map(lambda s: int(s) - 1, input().rstrip().split(' ')))

start = []
end = []
left = 0
for i in range(M):
    a, b, c, d = map(lambda s: int(s) - 1, input().rstrip().split(' '))
    board[a][b] = 10 + i
    start.append([a, b])
    end.append([c, d])
    left += 1

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while left > 0:
    # 승객 찾기
    dist = 0
    target = [N, N]
    found = False
    if board[car[0]][car[1]] >= 10:
        found = True
        target = car[:]
    else:
        queue = deque([[car, 0]])
        visited = [[False] * N for _ in range(N)]
        visited[car[0]][car[1]] = True
        while len(queue) > 0:
            [x, y], cur_dist = queue.popleft()
            if found and cur_dist >= dist:
                continue
            for d in dirs:
                dx, dy = x + d[0], y + d[1]
                if dx < 0 or dx >= N or dy < 0 or dy >= N or board[dx][dy] == 1 or visited[dx][dy]:
                    continue
                if board[dx][dy] == 0:
                    visited[dx][dy] = True
                    queue.append([[dx, dy], cur_dist + 1])
                elif board[dx][dy] >= 10:
                    if not found:
                        found = True
                        target = [dx, dy]
                        dist = cur_dist + 1
                    else:
                        if cur_dist + 1 < dist:
                            target = [dx, dy]
                            dist = cur_dist + 1
                        elif cur_dist + 1 == dist:
                            if dx < target[0] or (dx == target[0] and dy < target[1]):
                                target = [dx, dy]
                                dist = cur_dist + 1
    if not found:
        break
    # 승객에게 이동
    if dist > L:
        break
    L -= dist
    pnum = board[target[0]][target[1]] - 10  # 승객 번호
    board[target[0]][target[1]] = 0
    car = target[:]
    # 목적지 찾기
    destination = end[pnum]
    dist = 0
    target = [-1, -1]
    found = False
    queue = deque([[car, 0]])
    visited = [[False] * N for _ in range(N)]
    visited[car[0]][car[1]] = True
    while len(queue) > 0:
        [x, y], cur_dist = queue.popleft()
        for d in dirs:
            dx, dy = x + d[0], y + d[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N or board[dx][dy] == 1 or visited[dx][dy]:
                continue
            if dx == destination[0] and dy == destination[1]:
                found = True
                target = [dx, dy]
                dist = cur_dist + 1
                break
            else:
                visited[dx][dy] = True
                queue.append([[dx, dy], cur_dist + 1])

        if found:
            break
    if not found:
        break
    # 목적지로 이동
    if dist > L:
        break
    L += dist
    car = target[:]

    left -= 1

if left > 0:
    print(-1)
else:
    print(L)
