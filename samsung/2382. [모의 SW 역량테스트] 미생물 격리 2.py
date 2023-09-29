import sys
sys.stdin = open("input.txt", "r")

T = int(input())
four = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
for test_case in range(1, T + 1):
    N, M, K = map(int, input().rstrip().split())
    board = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        x, y, n, d = map(int, input().rstrip().split())
        board[x][y] = [n, four[d], [n, four[d]]]

    for _ in range(M):
        next_board = [[[] for _ in range(N)] for _ in range(N)]
        for cx in range(N):
            for cy in range(N):
                if len(board[cx][cy]) == 0:
                    continue
                cn, cd, _ = board[cx][cy]
                nx, ny, nn, nd = cx + cd[0], cy + cd[1], cn, cd
                if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                    nn = cn // 2
                    nd = [-cd[0], -cd[1]]

                if len(next_board[nx][ny]) == 0:
                    next_board[nx][ny] = [nn, nd, [nn, nd]]
                else:
                    xn, xd, [yn, yd] = next_board[nx][ny]
                    if nn > yn:
                        next_board[nx][ny] = [xn + nn, nd, [nn, nd]]
                    else:
                        next_board[nx][ny] = [xn + nn, xd, [yn, yd]]
        board = next_board
    count = 0
    for r in range(N):
        for c in range(N):
            if len(board[r][c]) == 0:
                continue
            count += board[r][c][0]
    print(f'#{test_case} {count}')
