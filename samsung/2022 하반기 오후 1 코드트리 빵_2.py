import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print(' ')

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

four = [[-1, 0], [0, -1], [0, 1], [1, 0]]
N, M = map(int, input().rstrip().split(' '))
board = [] # 0 빈공간, 1 베이스캠프, -1 벽
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
conv = []
for _ in range(M):
    x, y = map(int, input().rstrip().split(' '))
    conv.append([x - 1, y - 1])
t = 0
left = M
people = [None] * M
while left > 0:
    next_board = [board[i][:] for i in range(N)]
    # 사람 이동
    for pi in range(M):
        if people[pi] is None:
            continue
        cx, cy = conv[pi]
        px, py = people[pi]
        queue = deque([[px, py, [[px, py]]]])  # x, y, path
        visited = [[False] * N for _ in range(N)]
        visited[px][py] = True
        conv_path = []
        while len(queue) > 0:
            x, y, path = queue.popleft()
            if [x, y] == [cx, cy]:
                conv_path = path
                break
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] >= 0:
                    queue.append([nx, ny, path + [[nx, ny]]])
                    visited[nx][ny] = True
        npx, npy = conv_path[1]
        if [npx, npy] == [cx, cy]:
            next_board[cx][cy] = -1
            people[pi] = None
            left -= 1
        else:
            people[pi] = [npx, npy]
    board = next_board
    # 베이스캠프 출발
    if t < len(people):
        cx, cy = conv[t]
        queue = deque([[cx, cy, 0]])
        visited = [[False] * N for _ in range(N)]
        visited[cx][cy] = True
        min_dist = float('inf')
        min_camp = [-1, -1]
        while len(queue) > 0:
            x, y, dist = queue.popleft()
            if dist > min_dist:
                continue
            if board[x][y] == 1:
                if dist < min_dist:
                    min_dist = dist
                    min_camp = [x, y]
                elif dist == min_dist:
                    if [x, y] < min_camp:
                        min_camp = [x, y]
                continue
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] >= 0:
                    queue.append([nx, ny, dist + 1])
                    visited[nx][ny] = True
        people[t] = min_camp
        board[min_camp[0]][min_camp[1]] = -1
    t += 1
print(t)

# 벽이 생성되는 시점이 모든 사람이 이동한 후이다. (사람 이동 -> 벽 막힘 -> 베이스캠프 출발)이 맞는데 (사람 이동 -> 베이스캠프 출발 -> 벽 막힘) 해서 틀림
