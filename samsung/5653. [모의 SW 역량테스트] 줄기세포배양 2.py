T = int(input())
four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for test_case in range(1, T + 1):
    N, M, K = map(int, input().rstrip().split(' '))
    board = [[[] for _ in range(500)] for _ in range(500)]
    cells = []
    for n in range(N):
        l = list(map(int, input().strip().split(' ')))
        for m in range(M):
            if l[m] != 0:
                board[225 + n][225 + m] = [l[m], 1, l[m]]
                cells.append([225 + n, 225 + m, l[m], 1, l[m]])

    for k in range(K):
        next_cells = []
        for cx, cy, ct, cs, co in cells:
            if cs == 1:  # 비활성
                if ct == 1:
                    next_cells.append([cx, cy, co, 2, co])
                    board[cx][cy] = [co, 2, co]
                else:
                    next_cells.append([cx, cy, ct - 1, 1, co])
                    board[cx][cy] = [ct - 1, 1, co]
            elif cs == 2:  # 활성
                if ct == co:  # 번식
                    for dx, dy in four:
                        if len(board[cx + dx][cy + dy]) == 0:
                            next_cells.append([cx + dx, cy + dy, co, 1, co])
                            board[cx + dx][cy + dy] = [co, 1, co]
                        else:
                            xt, xs, xo = board[cx + dx][cy + dy]
                            if xt == xo and xs == 1 and xo < co:
                                for i in range(len(next_cells)) :
                                    if next_cells[i][0] == cx + dx and next_cells[i][1] == cy + dy:
                                        next_cells[i][2] = co
                                        next_cells[i][4] = co
                                        break
                                board[cx + dx][cy + dy] = [co, 1, co]
                if ct == 1:  # 사망
                    board[cx][cy] = [0, -1, co]
                else:
                    next_cells.append([cx, cy, ct - 1, 2, co])
                    board[cx][cy] = [ct - 1, 2, co]
        cells = next_cells
        # print(cells)
    print(f'#{test_case} {len(cells)}')
