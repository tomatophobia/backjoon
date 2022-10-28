import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().rstrip().split(' '))

board = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

cmd = list(map(int, input().rstrip().split(' ')))

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = [[[0] * 3 for _ in range(3)] for _ in range(3)]

cur = (x, y)
for c in cmd:
    d = directions[c - 1]
    next = (cur[0] + d[0], cur[1] + d[1])

    if next[0] < 0 or next[0] >= N or next[1] < 0 or next[1] >= M:
        continue
    cur = next
    if c == 1:  # 동
        dice[1][0][0], dice[0][0][-1], dice[-1][0][0], dice[0][0][1] = dice[0][0][1], dice[1][0][0], dice[0][0][-1], \
                                                                       dice[-1][0][0]
    elif c == 2:  # 서
        dice[1][0][0], dice[0][0][-1], dice[-1][0][0], dice[0][0][1] = dice[0][0][-1], dice[-1][0][0], dice[0][0][1], \
                                                                       dice[1][0][0]
    elif c == 3:  # 북
        dice[0][1][0], dice[0][0][-1], dice[0][-1][0], dice[0][0][1] = dice[0][0][1], dice[0][1][0], dice[0][0][-1], \
                                                                       dice[0][-1][0]
    elif c == 4:  # 남
        dice[0][1][0], dice[0][0][-1], dice[0][-1][0], dice[0][0][1] = dice[0][0][-1], dice[0][-1][0], dice[0][0][1], \
                                                                       dice[0][1][0]

    if board[cur[0]][cur[1]] == 0:
        board[cur[0]][cur[1]] = dice[0][0][-1]
    else:
        dice[0][0][-1] = board[cur[0]][cur[1]]
        board[cur[0]][cur[1]] = 0
    print(dice[0][0][1])
