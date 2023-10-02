import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

four = [[-1, 0], [0, -1], [0, 1], [1, 0]]
N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
conv = []
for _ in range(M):
    x, y = map(int, input().rstrip().split())
    conv.append([x - 1, y - 1])

people = [[] for _ in range(M)]

t = 0
left = M
while left > 0:
    t += 1
    for pp in range(M):
        if len(people[pp]) == 0:  # 아직 베이스캠프 도착하지 않음
            break
        if len(people[pp]) == 3:  # 편의점에 도착
            continue
        px, py = people[pp]
        cx, cy = conv[pp]
        # 1. 움직임
        queue = deque([[px, py, []]])
        visited = [[False] * N for _ in range(N)]
        best_move = []
        while len(queue) > 0:
            xx, yy, path = queue.popleft()
            if [xx, yy] == [cx, cy]:
                best_move = path[0]
                break
            for dx, dy in four:
                nx, ny = xx + dx, yy + dy
                if 0 <= nx < N and 0 <= ny < N and (board[nx][ny] >= 0 or board[nx][ny] <= -t) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, path + [[nx, ny]]])
        people[pp] = best_move
        # 2. 편의점 도착, 다음 턴 부터 막힘
        if people[pp] == [cx, cy]:
            left -= 1
            people[pp].append(True)
            board[cx][cy] = -t
    # 3. 베이스 캠프 시작
    if t > M:
        continue
    cx, cy = conv[t - 1]
    queue = deque([[cx, cy]])
    visited = [[False] * N for _ in range(N)]
    best_camp = []
    while len(queue) > 0:
        xx, yy = queue.popleft()
        if board[xx][yy] == 1:
            best_camp = [xx, yy]
            break
        for dx, dy in four:
            nx, ny = xx + dx, yy + dy
            if 0 <= nx < N and 0 <= ny < N and (board[nx][ny] >= 0 or board[nx][ny] < -t) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
    bx, by = best_camp
    people[t - 1] = [bx, by]
    board[bx][by] = -t
print(t)

# 이동 판단에 BFS를 써야 했는데 그리디로 생각했다. 너무 쉽다면 의심할 것. 웬만하면 1번 문제는 그래프를 쓴다.
