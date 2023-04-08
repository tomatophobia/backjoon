import sys
sys.stdin = open("input.txt", "r")

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().rstrip().split(" "))
    board = [[[0, 0]] * N for _ in range(N)]
    for _ in range(K):
        x, y, n, d = map(int, input().rstrip().split(" "))
        board[x][y] = [n, d - 1]

    for _ in range(M):
        next_board = [[[] for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if board[x][y][0] == 0:
                    continue
                n, d = board[x][y]
                dx, dy = x + dirs[d][0], y + dirs[d][1]
                if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:
                    n = n // 2
                    if d < 2:
                        d = (d + 1) % 2
                    else:
                        d = (d - 1) % 2 + 2
                if n > 0:
                    next_board[dx][dy].append([n, d])
        board = [[[0, 0]] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if len(next_board[x][y]) == 0:
                    continue
                elif len(next_board[x][y]) == 1:
                    board[x][y] = next_board[x][y][0]
                else:
                    sum_n = 0
                    max_n = 0
                    max_d = 0
                    for n, d in next_board[x][y]:
                        sum_n += n
                        if n > max_n:
                            max_n = n
                            max_d = d
                    board[x][y] = [sum_n, max_d]
    count = 0
    for x in range(N):
        for y in range(N):
            count += board[x][y][0]
    print(f"#{test_case} {count}")
