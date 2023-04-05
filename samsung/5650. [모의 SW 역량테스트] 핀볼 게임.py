import sys
sys.stdin = open("input.txt", "r")

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N = int(input().rstrip())

    board = []
    worm = []
    for n in range(N):
        line = list(map(int, input().rstrip().split(' ')))
        board.append(line)
        for m in range(N):
            if line[m] >= 6:
                worm.append([line[m], n, m])

    max_score = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0:
                continue
            for d in dirs:
                score = 0
                rr, cc, dd = r, c, d
                while True:
                    nr, nc = rr + dd[0], cc + dd[1]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        dd = [-dd[0], -dd[1]]
                        score += 1
                    elif board[nr][nc] == 1:
                        if dd == [0, 1] or dd == [-1, 0]:
                            dd = [-dd[0], -dd[1]]
                        else:
                            dd = [dd[1], dd[0]]
                        score += 1
                    elif board[nr][nc] == 2:
                        if dd == [0, 1] or dd == [1, 0]:
                            dd = [-dd[0], -dd[1]]
                        else:
                            dd = [-dd[1], -dd[0]]
                        score += 1
                    elif board[nr][nc] == 3:
                        if dd == [0, -1] or dd == [1, 0]:
                            dd = [-dd[0], -dd[1]]
                        else:
                            dd = [dd[1], dd[0]]
                        score += 1
                    elif board[nr][nc] == 4:
                        if dd == [0, -1] or dd == [-1, 0]:
                            dd = [-dd[0], -dd[1]]
                        else:
                            dd = [-dd[1], -dd[0]]
                        score += 1
                    elif board[nr][nc] == 5:
                        dd = [-dd[0], -dd[1]]
                        score += 1
                    elif 6 <= board[nr][nc] <= 10:
                        for w in worm:
                            if w[0] == board[nr][nc] and (nr != w[1] or nc != w[2]):
                                nr, nc = w[1], w[2]
                                break
                    rr, cc = nr, nc

                    if (rr == r and cc == c) or (0 <= rr < N and 0 <= cc < N and board[rr][cc]) == -1:
                        break
                if score > max_score:
                    max_score = score

    print(f"#{test_case} {max_score}")
