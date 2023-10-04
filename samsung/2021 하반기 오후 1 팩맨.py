import sys
sys.stdin = open('input.txt', 'r')

def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]:10}', end='')
        print('')


from collections import deque

def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
eight = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
four = [[-1, 0], [0, -1], [1, 0], [0, 1]]
four.reverse()
M, T = map(int, input().rstrip().split(' '))
R, C = map(int, input().rstrip().split(' '))
pacman = [R - 1, C - 1]
board = [[[[], 0] for _ in range(4)] for _ in range(4)]  # [[알], 시체]
monster = []
for _ in range(M):
    r, c, d = map(int, input().rstrip().split(' '))
    monster.append([r - 1, c - 1, d - 1])

for _ in range(T):
    # 1. 몬스터 복제
    for mx, my, md in monster:
        board[mx][my][0].append(md)
    # 2. 몬스터 이동
    for mm in monster:
        nx, ny, nd = mm
        for i in range(8):
            nd = (mm[2] + i) % 8
            nx, ny = mm[0] + eight[nd][0], mm[1] + eight[nd][1]
            if is_valid(nx, ny, 4) and board[nx][ny][1] == 0 and [nx, ny] != pacman:
                mm[0], mm[1], mm[2] = nx, ny, nd
                break
    # 3. 팩맨 이동
    best_move = []
    best_score = -1
    px, py = pacman
    stack = [[px, py, [], 0]]
    dcount = 0
    while len(stack) > 0:
        cx, cy, cp, cs = stack.pop()
        if len(cp) == 3:
            if cs > best_score:
                best_score = cs
                best_move = cp
            continue
        for dx, dy in four:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, 4):
                score = 0
                if [nx, ny] not in cp:
                    for mx, my, _ in monster:
                        if [nx, ny] == [mx, my]:
                            score += 1
                stack.append([nx, ny, cp + [[nx, ny]], cs + score])
    pacman = best_move[-1]
    # 시체 소멸
    for x in range(4):
        for y in range(4):
            if board[x][y][1] > 0:
                board[x][y][1] -= 1
    # 팩맨 움직임
    next_monster = []
    for mx, my, md in monster:
        if [mx, my] in best_move:
            board[mx][my][1] = 2
        else:
            next_monster.append([mx, my, md])
    # 복제 완료
    for x in range(4):
        for y in range(4):
            if len(board[x][y][0]) > 0:
                for md in board[x][y][0]:
                    next_monster.append([x, y, md])
                board[x][y][0] = []
    monster = next_monster

print(len(monster))

# 우선 순위를 위한 점수 계산에서 실수가 잦다.
# 한 번에 맞추지 못하더라도 내가 점수 계산에서 어떤 부분을 실수했을지 잘 생각해보자.
# 확실한 BFS, DFS가 아니고 brute force로 쉽게 풀 수 있다면 그냥 brute force로 가자.
# N이 작더라도 반복하면서 증식할 수 있으니 시간복잡도, 공간복잡도 방심하지 않기
