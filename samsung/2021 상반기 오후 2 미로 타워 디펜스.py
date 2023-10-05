import sys

sys.stdin = open('input.txt', 'r')


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def board_to_list(board):
    N = len(board)
    x, y, d = N // 2, N // 2, 2
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    result = []
    while True:
        nx, ny = x + four[d][0], y + four[d][1]
        if not is_valid(nx, ny, N):
            break
        visited[nx][ny] = True
        if board[nx][ny] > 0:
            result.append(board[nx][ny])
        x, y = nx, ny
        # 꺾어보기
        nd = (d - 1) % 4
        nx, ny = x + four[nd][0], y + four[nd][1]
        if visited[nx][ny]:
            nd = d
        d = nd
    return result


def list_to_board(elist, N):
    x, y, d = N // 2, N // 2, 2
    board = [[0] * N for _ in range(N)]
    idx = 0
    while True:
        nx, ny = x + four[d][0], y + four[d][1]
        if not is_valid(nx, ny, N):
            break
        board[nx][ny] = elist[idx]
        idx += 1
        if idx == len(elist):
            break
        x, y = nx, ny
        # 꺾어보기
        nd = (d - 1) % 4
        nx, ny = x + four[nd][0], y + four[nd][1]
        if board[nx][ny] > 0 or [nx, ny] == [N // 2, N // 2]:
            nd = d
        d = nd
    return board


four = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))

score = 0
tx, ty = N // 2, N // 2
for _ in range(M):
    # 입력
    d, p = map(int, input().rstrip().split(' '))
    # 레이저 공격
    for i in range(1, p + 1):
        nx, ny = tx + four[d][0] * i, ty + four[d][1] * i
        score += board[nx][ny]
        board[nx][ny] = 0
    # 4 이상 반복 삭제
    enemies = board_to_list(board)
    if len(enemies) == 0:
        break
    while True:
        end = True
        next_enemies = []
        stack = [enemies[0]]
        for e in enemies[1:]:
            if stack[-1] == e:
                stack.append(e)
            else:
                if len(stack) >= 4:
                    end = False
                    score += stack[-1] * len(stack)
                    stack = [e]
                else:
                    next_enemies += stack
                    stack = [e]
        if len(stack) >= 4:
            end = False
            score += stack[-1] * len(stack)
            stack = []
        enemies = next_enemies + stack
        if end:
            break
    # 증식
    next_enemies = []
    stack = [enemies[0]]
    for e in enemies[1:]:
        if stack[-1] == e:
            stack.append(e)
        else:
            next_enemies.append(len(stack))
            next_enemies.append(stack[-1])
            stack = [e]
    if len(stack) > 0:
        next_enemies.append(len(stack))
        next_enemies.append(stack[-1])
    enemies = next_enemies
    # board에 입력
    board = list_to_board(enemies, N)
print(score)
