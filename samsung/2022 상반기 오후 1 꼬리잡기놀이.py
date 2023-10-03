import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M, K = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# BFS 팀 구성하기 O(N^2 + E), E = 2N(N-1)
teams = [[False, []]]  # [bool, list] => True면 왼쪽이 앞, False면 오른쪽이 앞
team_idx = 0
for r in range(N):
    for c in range(N):
        if board[r][c] != 1:
            continue
        team_idx += 1
        stack = [[r, c, []]]
        worm = deque([[r, c]])
        board[r][c] = -team_idx
        while len(stack) > 0:
            cx, cy, before = stack.pop()
            for dx, dy in four:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < N and [nx, ny] != before:
                    if board[nx][ny] == 2:
                        stack.append([nx, ny, [cx, cy]])
                        worm.append([nx, ny])
                        board[nx][ny] = -team_idx
        cx, cy = worm[-1]
        for dx, dy in four:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 3:
                worm.append([nx, ny])
                board[nx][ny] = -team_idx
        teams.append([True, worm])
# 라운드 진행
ball = [[i, 0, [0, 1]] for i in range(N)] + [[N - 1, i, [-1, 0]] for i in range(N)] + [[N - 1 - i, N - 1, [0, -1]] for i
                                                                                       in range(N)] + [
           [0, N - 1 - i, [1, 0]] for i in range(N)]
k = 0
point = 0
for _ in range(K):
    # 이동
    for tb, worm in teams:
        if len(worm) == 0:
            continue
        if tb:  # 왼쪽이 앞
            tx, ty = worm.pop()
            hx, hy = worm[0]
            for dx, dy in four:
                nx, ny = hx + dx, hy + dy
                if (0 <= nx < N and 0 <= ny < N and board[nx][ny] == 4) or [nx, ny] == [tx, ty]:
                    worm.appendleft([nx, ny])
                    board[nx][ny], board[tx][ty] = board[tx][ty], board[nx][ny]
                    break
        else:  # 오른쪽이 앞
            tx, ty = worm.popleft()
            hx, hy = worm[-1]
            for dx, dy in four:
                nx, ny = hx + dx, hy + dy
                if (0 <= nx < N and 0 <= ny < N and board[nx][ny] == 4) or [nx, ny] == [tx, ty]:
                    worm.append([nx, ny])
                    board[nx][ny], board[tx][ty] = board[tx][ty], board[nx][ny]
                    break
    # 공던지기
    bx, by, [dx, dy] = ball[k]
    while 0 <= bx < N and 0 <= by < N and board[bx][by] >= 0:
        bx, by = bx + dx, by + dy
    if 0 <= bx < N and 0 <= by < N:
        team = teams[-board[bx][by]]
        for tidx in range(len(team[1])):
            if team[1][tidx] == [bx, by]:
                if team[0]:
                    point += (tidx + 1) ** 2
                else:
                    point += (len(team[1]) - tidx) ** 2
                break
        team[0] = not team[0]
    k = (k + 1) % len(ball)
print(point)

# 범위 조건 and 리스트 조건 => 순서 지키기
# 점수 계산할 때 머리가 어디냐에 따라 계산법 달라짐
# 머리와 꼬리가 이어져있을 때를 제대로 처리하지 못해서 엄청 오래 걸림
# 처음 팀 정하기에서도 오래걸리고 움직이기 코드도 수정하느라 오래걸림
