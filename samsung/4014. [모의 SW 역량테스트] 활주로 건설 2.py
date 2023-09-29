import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().rstrip().split(' '))
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split())))
    count = 0
    # 가로
    for r in range(N):
        road = [False] * N
        success = True
        for x in range(N - 1):
            if board[r][x] - board[r][x + 1] == 1:
                for xx in range(x + 1, x + 1 + X):
                    if xx >= N or road[xx] or board[r][xx] != board[r][x + 1]:
                        success = False
                        break
                    road[xx] = True
                if not success:
                    break
            elif board[r][x] - board[r][x + 1] == -1:
                for xx in range(x, x - X, -1):
                    if xx < 0 or road[xx] or board[r][xx] != board[r][x]:
                        success = False
                        break
                    road[xx] = True
                if not success:
                    break
            elif board[r][x] == board[r][x + 1]:
                continue
            else:
                success = False
                break
        if success:
            count += 1
    # 세로
    for c in range(N):
        road = [False] * N
        success = True
        for x in range(N - 1):
            if board[x][c] - board[x + 1][c] == 1:
                for xx in range(x + 1, x + 1 + X):
                    if xx >= N or road[xx] or board[xx][c] != board[x + 1][c]:
                        success = False
                        break
                    road[xx] = True
                if not success:
                    break
            elif board[x][c] - board[x + 1][c] == -1:
                for xx in range(x, x - X, -1):
                    if xx < 0 or road[xx] or board[xx][c] != board[x][c]:
                        success = False
                        break
                    road[xx] = True
                if not success:
                    break
            elif board[x][c] == board[x + 1][c]:
                continue
            else:
                success = False
                break
        if success:
            count += 1
    print(f'#{test_case} {count}')
