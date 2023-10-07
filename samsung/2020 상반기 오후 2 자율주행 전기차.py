import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


four = [[-1, 0], [0, -1], [0, 1], [1, 0]]
N, M, C = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
cx, cy = map(lambda x: int(x) - 1, input().rstrip().split(' '))
cc = C
arrival = [[]]
for i in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split(' '))
    board[x1 - 1][y1 - 1] = - (i + 1)
    arrival.append([x2 - 1, y2 - 1])

for _ in range(M):
    fx, fy, fc, fn = -1, -1, float('inf'), 0
    # 현재 위치에 있을 때
    if board[cx][cy] < 0:
        fx, fy, fc, fn = cx, cy, 0, board[cx][cy]
    else:
        # BFS로 가까운 사람 찾기
        queue = deque([[cx, cy, 0]])
        visited = [[False] * N for _ in range(N)]
        visited[cx][cy] = True
        while len(queue) > 0:
            x, y, dist = queue.popleft()
            if dist > fc:
                continue
            if board[x][y] < 0:
                if dist < fc:
                    fx, fy, fc, fn = x, y, dist, board[x][y]
                elif [x, y] < [fx, fy]:
                    fx, fy, fc, fn = x, y, dist, board[x][y]
                continue
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] != 1:
                    queue.append([nx, ny, dist + 1])
                    visited[nx][ny] = True
    if fc >= cc or [fx, fy] == [-1, -1]:
        cc = -1
        break
    board[fx][fy] = 0
    cx, cy, cc = fx, fy, cc - fc
    # 목적지 BFS
    ax, ay = arrival[-fn]
    queue = deque([[cx, cy, 0]])
    visited = [[False] * N for _ in range(N)]
    visited[cx][cy] = True
    a_dist = -1
    while len(queue) > 0:
        x, y, dist = queue.popleft()
        if [x, y] == [ax, ay]:
            a_dist = dist
            break
        for dx, dy in four:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, N) and not visited[nx][ny] and board[nx][ny] != 1:
                queue.append([nx, ny, dist + 1])
                visited[nx][ny] = True
    if a_dist > cc or a_dist == -1:
        cc = -1
        break
    cx, cy, cc = ax, ay, cc + a_dist
print(cc)
# 그래프 상에서 연결이 끊겨있을 때 생각하기
