import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


four = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, K = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
history = [[0] * M for _ in range(N)]

for k in range(1, K + 1):
    # 공격자와 대상자 선정
    attack = [-1, -1]
    # score = [공격력, -마지막 공격 시각, -(행 + 열), -열]
    attack_score = [float('inf'), float('inf'), float('inf'), float('inf')]
    target = [-1, -1]
    target_score = [-float('inf'), -float('inf'), -float('inf'), -float('inf')]
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                continue
            score = [board[r][c], -history[r][c], -(r + c), -c]
            if score < attack_score:
                attack_score = score
                attack = [r, c]
            if score > target_score:
                target_score = score
                target = [r, c]
    if attack == target:  # 포탑 하나만 남음
        break
    ax, ay = attack
    tx, ty = target
    history[ax][ay] = k
    board[ax][ay] += N + M
    # 공격 가능 여부 확인 (BFS)
    queue = deque([[ax, ay, [[ax, ay]]]])  # [x, y, path]
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True
    best_path = []
    while len(queue) > 0:
        x, y, path = queue.popleft()
        if [x, y] == target:
            best_path = path
            break
        for dx, dy in four:
            nx, ny = (x + dx) % N, (y + dy) % M
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            queue.append([nx, ny, path + [[nx, ny]]])
            visited[nx][ny] = True
    fight = [[False] * M for _ in range(N)]  # 공격에 연루된 모든 포탑
    fight[ax][ay] = True
    fight[tx][ty] = True
    if len(best_path) != 0:
        # 레이저 공격
        for bx, by in best_path[1:-1]:
            board[bx][by] = max(board[bx][by] - board[ax][ay] // 2, 0)
            fight[bx][by] = True
        board[tx][ty] = max(board[tx][ty] - board[ax][ay], 0)
    else:
        # 포탑 공격
        for dx, dy in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
            nx, ny = (tx + dx) % N, (ty + dy) % M
            if board[nx][ny] == 0 or [nx, ny] == attack:
                continue
            board[nx][ny] = max(board[nx][ny] - board[ax][ay] // 2, 0)
            fight[nx][ny] = True
        board[tx][ty] = max(board[tx][ty] - board[ax][ay], 0)
    # 체력 회복
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0 or fight[r][c]:
                continue
            board[r][c] += 1
strongest = 0
for r in range(N):
    for c in range(M):
        if board[r][c] > strongest:
            strongest = board[r][c]
print(strongest)

# 공격 히스토리 만들어놓고 안쓴 실수
# 포탑 공격 후 음수가 되지 않게 0으로 만들지 않은 실수 (심지어 저번에 했던 실수임)
