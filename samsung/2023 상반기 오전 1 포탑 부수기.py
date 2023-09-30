import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

four = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, K = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

atk_history = [[0] * M for _ in range(N)]
t = 0
for _ in range(K):
    t += 1
    # 공격자, 타겟 선정
    ax, ay = -1, -1
    min_atk = float('inf')
    tx, ty = -1, -1
    max_atk = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:
                continue
            if board[x][y] < min_atk:
                min_atk = board[x][y]
                ax, ay = x, y
            elif board[x][y] == min_atk:
                if atk_history[x][y] > atk_history[ax][ay]:
                    ax, ay = x, y
                elif atk_history[x][y] == atk_history[ax][ay]:
                    if x + y > ax + ay:
                        ax, ay = x, y
                    elif x + y == ax + ay:
                        if y > ay:
                            ax, ay = x, y
            if board[x][y] > max_atk:
                max_atk = board[x][y]
                tx, ty = x, y
            elif board[x][y] == max_atk:
                if atk_history[x][y] < atk_history[tx][ty]:
                    tx, ty = x, y
                elif atk_history[x][y] == atk_history[tx][ty]:
                    if x + y < tx + ty:
                        tx, ty = x, y
                    elif x + y == tx + ty:
                        if y < ty:
                            tx, ty = x, y
    # 종료 조건
    if [ax, ay] == [tx, ty]:
        break
    # 공격자 핸디캡, 공격 역사 기록
    board[ax][ay] += N + M
    atk_history[ax][ay] = t
    # 공격
    target = [[False] * M for _ in range(N)]
    target[ax][ay] = True
    target[tx][ty] = True
    # 최단거리 경로찾기, BFS
    visited = [[False] * M for _ in range(N)]
    queue = deque([[ax, ay, []]])
    visited[ax][ay] = True
    find = False
    while len(queue) > 0:
        x, y, path = queue.popleft()
        if [x, y] == [tx, ty]:
            find = True
            for px, py in path[:-1]:
                target[px][py] = True
                board[px][py] = max(board[px][py] - board[ax][ay] // 2, 0)
            board[tx][ty] = max(board[tx][ty] - board[ax][ay], 0)
            break
        for dx, dy in four:
            nx, ny = (x + dx) % N, (y + dy) % M
            if board[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append([nx, ny, path + [[nx, ny]]])
            visited[nx][ny] = True
    # 못 찾으면 포탑공격
    if not find:
        for dx, dy in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
            nx, ny = (tx + dx) % N, (ty + dy) % M
            if [nx, ny] == [ax, ay]:
                continue
            target[nx][ny] = True
            board[nx][ny] = max(board[nx][ny] - board[ax][ay] // 2, 0)
        board[tx][ty] = max(board[tx][ty] - board[ax][ay], 0)
    # 포탑 수복
    for x in range(N):
        for y in range(M):
            if target[x][y] or board[x][y] == 0:
                continue
            board[x][y] += 1

final_atk = 0
for x in range(N):
    for y in range(M):
        if board[x][y] > final_atk:
            final_atk = board[x][y]
print(final_atk)
