import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
start = [0, 0]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
queue = deque([[start, 0, 1]])
visited[0][0][0] = True

fail = True
while len(queue) > 0:
    pos, wall, size = queue.popleft()
    if pos == [N - 1, M - 1]:
        fail = False
        print(size)
        break
    for dx, dy in dirs:
        nx, ny = pos[0] + dx, pos[1] + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny][wall]:
            continue

        if wall == 0 and board[nx][ny] == '1':
            visited[nx][ny][1] = True
            queue.append([[nx, ny], 1, size + 1])
        elif board[nx][ny] == '0':
            visited[nx][ny][wall] = True
            queue.append([[nx, ny], wall, size + 1])

if fail:
    print(-1)

# 놀라운 배움! => 가중치가 없는 그래프에서 BFS로 최단거리를 구할 수 있다. 따라서 큐에다가 visited를 넣지 않아도 괜찮다. 똑같은 도착지로 가는 경로가 2개일 때 둘 중 어느 것으로 가도 상관 없으니까!
