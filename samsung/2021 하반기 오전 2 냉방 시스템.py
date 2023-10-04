import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f"{board[r][c]:5}", end='')
        print('')


four = [[0, -1], [-1, 0], [0, 1], [1, 0]]
N, M, K = map(int, input().rstrip().split(' '))
board = [[0] * N for _ in range(N)]
edge = [[[0, 1, 2, 3] for _ in range(N)] for _ in range(N)]
aircon = []
people = []
for x in range(N):
    ll = list(map(int, input().rstrip().split(' ')))
    for y in range(N):
        if ll[y] == 1:
            people.append([x, y])
        elif ll[y] > 1:
            aircon.append([x, y, ll[y] - 2])
for _ in range(M):
    x, y, s = map(int, input().rstrip().split(' '))
    if s == 0:  # 위
        if 1 in edge[x - 1][y - 1]:
            edge[x - 1][y - 1].remove(1)
        if 3 in edge[x - 2][y - 1]:
            edge[x - 2][y - 1].remove(3)
    elif s == 1:  # 왼
        if 0 in edge[x - 1][y - 1]:
            edge[x - 1][y - 1].remove(0)
        if 2 in edge[x - 1][y - 2]:
            edge[x - 1][y - 2].remove(2)
t = 0
while True:
    # 조건 확인
    success = True
    for px, py in people:
        if board[px][py] < K:
            success = False
            break
    if success:
        break
    t += 1
    if t == 101:
        t = -1
        break

    # 에어컨 바람 전파
    next_board = [board[i][:] for i in range(N)]
    for ax, ay, ad in aircon:
        nx, ny = ax + four[ad][0], ay + four[ad][1]
        queue = deque([[nx, ny, 4]])
        visited = [[False] * N for _ in range(N)]
        visited[nx][ny] = True
        next_board[nx][ny] += 5
        while len(queue) > 0:
            cx, cy, cc = queue.popleft()
            if cc == 0:
                continue
            # ad 방향
            if ad in edge[cx][cy]:
                nx, ny = cx + four[ad][0], cy + four[ad][1]
                if is_valid(nx, ny, N) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    next_board[nx][ny] += cc
                    queue.append([nx, ny, cc - 1])
            # ad - 1, ad 방향 & ad + 1, ad 방향
            for add in [(ad - 1) % 4, (ad + 1) % 4]:
                if add in edge[cx][cy]:
                    nx, ny = cx + four[add][0], cy + four[add][1]
                    if is_valid(nx, ny, N) and ad in edge[nx][ny]:
                        nx, ny = nx + four[ad][0], ny + four[ad][1]
                        if is_valid(nx, ny, N) and not visited[nx][ny]:
                            visited[nx][ny] = True
                            next_board[nx][ny] += cc
                            queue.append([nx, ny, cc - 1])
    board = next_board
    # 공기 섞임
    next_board = [board[i][:] for i in range(N)]
    for x in range(N):
        for y in range(N):
            for ddd in [2, 3]:
                if ddd in edge[x][y]:
                    nx, ny = x + four[ddd][0], y + four[ddd][1]
                    if is_valid(nx, ny, N):
                        diff = abs(board[nx][ny] - board[x][y]) // 4
                        if board[nx][ny] > board[x][y]:
                            next_board[x][y] += diff
                            next_board[nx][ny] -= diff
                        else:
                            next_board[x][y] -= diff
                            next_board[nx][ny] += diff
    board = next_board
    # 외벽 시원함 1 감소
    for c in range(N):
        if board[0][c] > 0:
            board[0][c] -= 1
    for r in range(1, N):
        for c in [0, N - 1]:
            if board[r][c] > 0:
                board[r][c] -= 1
    for c in range(1, N - 1):
        if board[N - 1][c] > 0:
            board[N - 1][c] -= 1
print(t)
