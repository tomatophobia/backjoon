import sys

sys.stdin = open('input.txt', 'r')


def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:4}', end='')
        print('')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


N, M, K = map(int, input().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split(' '))))
people = []
for _ in range(M):
    x, y = map(int, input().rstrip().split(' '))
    people.append([x - 1, y - 1])
ex, ey = map(lambda x: int(x) - 1, input().rstrip().split(' '))
total_move = 0
for _ in range(K):
    # 참가자 이동
    best_square = float('inf')
    best_square_pos = []
    for px, py in people:
        best_dist = abs(ex - px) + abs(ey - py)
        bx, by = px, py
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nx, ny = px + dx, py + dy
            if not is_valid(nx, ny, N) or board[nx][ny] > 0:
                continue
            dist = abs(ex - nx) + abs(ey - ny)
            if dist < best_dist:
                best_dist = dist
                bx, by = nx, ny
        if [px, py] != [bx, by]:
            total_move += 1
        if [bx, by] == [ex, ey]:
            continue
        board[bx][by] -= 1  # 사람 위치 표시, 여러 사람이 중복 위치에 있을 수 있다.
        # 정사각형 구하기
        square = max(abs(ex - bx), abs(ey - by))
        if square < best_square:
            best_square = square
            rd = [max(ex, bx), max(ey, by)]
            lu = [rd[0] - square, rd[1] - square]
            for idx in [0, 1]:
                while lu[idx] < 0:
                    lu[idx] += 1
                    rd[idx] += 1
            best_square_pos = [lu, rd]
        elif square == best_square:
            rd = [max(ex, bx), max(ey, by)]
            lu = [rd[0] - square, rd[1] - square]
            for idx in [0, 1]:
                while lu[idx] < 0:
                    lu[idx] += 1
                    rd[idx] += 1
            if len(best_square_pos) == 0 or lu < best_square_pos[0]:
                best_square_pos = [lu, rd]
    if len(best_square_pos) == 0:
        break  # 모두 탈출
    # 회전
    board[ex][ey] = -float('inf')  # 출구 표시
    lu, rd = best_square_pos
    square = best_square + 1
    temp = [[0] * square for _ in range(square)]
    for x in range(lu[0], rd[0] + 1):
        for y in range(lu[1], rd[1] + 1):
            to_move = board[x][y]
            if to_move > 0:
                to_move -= 1
            temp[y - lu[1]][square - 1 - (x - lu[0])] = to_move  # 평행이동 + 회전이동
    for x in range(square):
        for y in range(square):
            board[x + lu[0]][y + lu[1]] = temp[x][y]  # 평행이동
    # 출구와 사람 갱신
    next_people = []
    for x in range(N):
        for y in range(N):
            if board[x][y] < 0:
                if board[x][y] == -float('inf'):
                    ex, ey = x, y
                    board[x][y] = 0
                else:
                    for _ in range(-board[x][y]):
                        next_people.append([x, y])
                    board[x][y] = 0
    people = next_people
print(total_move)
print(ex + 1, ey + 1)

# 좌표를 출력할 때 zero-index에서 one-index로 바꿨는지 점검하기
# 사람이 한 좌표에 중복으로 서있을 수 있다는 점을 잊고 모두 뭉쳐서 -1로 표시했다. 이런 조건 조심하기
