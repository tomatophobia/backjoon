import sys

input = sys.stdin.readline

R, C, M = map(int, input().rstrip().split(' '))

direct = [None, (-1, 0), (1, 0), (0, 1), (0, -1)]
board = [[None] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().rstrip().split(' '))
    r -= 1
    c -= 1
    board[r][c] = (s, direct[d], z)

count = 0
for fisher in range(C):
    # 상어 낚기
    for i in range(R):
        shark = board[i][fisher]
        if shark is not None:
            count += shark[2]
            board[i][fisher] = None
            break
    # 상어 이동
    next_board = [[None] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            r = i
            c = j
            if board[r][c] is None:
                continue
            s, (dr, dc), z = board[r][c]
            left = s
            while left > 0:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    dr = -dr
                    dc = -dc
                    continue
                r, c = nr, nc
                left -= 1
            if next_board[r][c] is None or next_board[r][c][2] < z:
                next_board[r][c] = (s, (dr, dc), z)
    board = next_board
print(count)
