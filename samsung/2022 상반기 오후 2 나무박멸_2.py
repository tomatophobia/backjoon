import sys

sys.stdin = open('input.txt', 'r')


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


four = [[1, 0], [0, 1], [0, -1], [-1, 0]]
side_four = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
N, M, K, C = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
poison = [[0] * N for _ in range(N)]
kill = 0
for _ in range(M):
    # 나무 성장
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                near = 0
                for dx, dy in four:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, N) and board[nx][ny] > 0:
                        near += 1
                board[x][y] += near
    # 나무 번식
    next_board = [board[i][:] for i in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                child = []
                for dx, dy in four:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, N) and board[nx][ny] == 0 and poison[nx][ny] == 0:
                        child.append([nx, ny])
                for cx, cy in child:
                    next_board[cx][cy] += board[x][y] // len(child)
    board = next_board
    # 제초제 베스트 위치 찾기
    best_count = 0
    best_target = []
    for x in range(N):
        for y in range(N):
            if board[x][y] <= 0:
                continue
            count = board[x][y]
            target = [[x, y]]
            for dx, dy in side_four:
                for i in range(1, K + 1):
                    nx, ny = x + dx * i, y + dy * i
                    if not is_valid(nx, ny, N) or board[nx][ny] <= 0:
                        if is_valid(nx, ny, N):
                            target.append([nx, ny])
                        break
                    count += board[nx][ny]
                    target.append([nx, ny])
            if count > best_count:
                best_count = count
                best_target = target
    # 전년도 제초제 날아감
    for x in range(N):
        for y in range(N):
            if poison[x][y] > 0:
                poison[x][y] -= 1
    # 제초제 뿌리기
    kill += best_count
    for tx, ty in best_target:
        if board[tx][ty] > 0:
            board[tx][ty] = 0
        poison[tx][ty] = C
print(kill)
