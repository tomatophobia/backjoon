import sys

sys.stdin = open("input.txt", "r")

T = int(input())
four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    hole = [[] for _ in range(13)]
    for n in range(N):
        l = list(map(int, input().rstrip().split(' ')))
        for m in range(N):
            if l[m] > 5:
                hole[l[m]].append([n, m])
        board.append(l)

    max_score = 0
    for xx in range(N):
        for yy in range(N):
            if board[xx][yy] != 0:
                continue
            sx, sy = xx, yy
            for d in four:
                x, y = sx, sy
                dx, dy = d
                score = 0
                while True:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or nx >= N or ny < 0 or ny >= N) or board[nx][ny] == 5:
                        score *= 2
                        score += 1
                        break
                    elif board[nx][ny] == -1 or [sx, sy] == [nx, ny]:
                        break
                    elif board[nx][ny] == 0:
                        x, y = nx, ny
                    elif board[nx][ny] == 1:
                        if [dx, dy] == [-1, 0] or [dx, dy] == [0, 1]:
                            score *= 2
                            score += 1
                            break
                        dx, dy = dy, dx
                        score += 1
                        x, y = nx, ny
                    elif board[nx][ny] == 2:
                        if [dx, dy] == [1, 0] or [dx, dy] == [0, 1]:
                            score *= 2
                            score += 1
                            break
                        dx, dy = -dy, -dx
                        score += 1
                        x, y = nx, ny
                    elif board[nx][ny] == 3:
                        if [dx, dy] == [1, 0] or [dx, dy] == [0, -1]:
                            score *= 2
                            score += 1
                            break
                        dx, dy = dy, dx
                        score += 1
                        x, y = nx, ny
                    elif board[nx][ny] == 4:
                        if [dx, dy] == [-1, 0] or [dx, dy] == [0, -1]:
                            score *= 2
                            score += 1
                            break
                        dx, dy = -dy, -dx
                        score += 1
                        x, y = nx, ny
                    elif board[nx][ny] > 5:
                        [[h1x, h1y], [h2x, h2y]] = hole[board[nx][ny]]
                        if [h1x, h1y] == [nx, ny]:
                            nx, ny = h2x, h2y
                        elif [h2x, h2y] == [nx, ny]:
                            nx, ny = h1x, h1y
                        else:
                            print("fail")
                        x, y = nx, ny
                if score > max_score:
                    max_score = score
    print(f'#{test_case} {max_score}')

# iterate 하고 있는 변수를 변경하지 말 것
