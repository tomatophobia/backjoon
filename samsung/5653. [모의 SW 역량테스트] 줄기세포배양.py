from queue import PriorityQueue
import sys

sys.stdin = open("input.txt", "r")

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().rstrip().split(' '))
    board = [[0] * 400 for _ in range(400)]

    cells = PriorityQueue()
    for n in range(N):
        line = list(map(int, input().rstrip().split(' ')))
        for m in range(M):
            c = line[m]
            if c > 0:
                board[n + 175][m + 175] = c
                cells.put([-c, n + 175, m + 175, False, c])  # 정렬 기준, 위치, 활성 여부, 남은 시간

    for _ in range(K):
        next_cells = PriorityQueue()
        while not cells.empty():
            cnum, x, y, active, time = cells.get()
            cnum = -cnum

            time -= 1
            if active:
                if cnum - 1 == time:
                    for d in dirs:
                        dx = x + d[0]
                        dy = y + d[1]
                        if board[dx][dy] == 0:
                            board[dx][dy] = cnum
                            next_cells.put([-cnum, dx, dy, False, cnum])

                if time > 0:
                    next_cells.put([-cnum, x, y, active, time])
                else:
                    board[x][y] = -1
            else:
                if time > 0:
                    next_cells.put([-cnum, x, y, active, time])
                else:
                    next_cells.put([-cnum, x, y, True, cnum])
        cells = next_cells

    count = 0
    for m in range(len(board)):
        for n in range(len(board[0])):
            if board[m][n] > 0:
                count += 1

    print(f"#{test_case} {count}")
