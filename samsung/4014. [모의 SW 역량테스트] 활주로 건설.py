import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, X = map(int, input().rstrip().split(" "))
    board = []
    for _ in range(N):
        line = list(map(int, input().rstrip().split(" ")))
        board.append(line)

    count = 0
    # row
    for i in range(N):
        failed = False
        blocked = [False] * N
        for j in range(1, N):
            curr = board[i][j]
            before = board[i][j - 1]
            if before == curr:
                continue
            elif abs(before - curr) > 1:
                failed = True
                break
            elif before < curr:
                for x in range(1, X+1):
                    if j - x < 0:
                        failed = True
                        break
                    before_x = board[i][j - x]
                    if before_x != before:
                        failed = True
                        break
                    if blocked[j-x]:
                        failed = True
                        break
                    blocked[j-x] = True
                if failed:
                    break
            else:
                for x in range(X):
                    if j + x >= N:
                        failed = True
                        break
                    after_x = board[i][j + x]
                    if after_x != curr:
                        failed = True
                        break
                    if blocked[j+x]:
                        failed = True
                        break
                    blocked[j+x] = True
                if failed:
                    break
        if not failed:
            count += 1

    # col
    for j in range(N):
        failed = False
        blocked = [False] * N
        for i in range(1, N):
            curr = board[i][j]
            before = board[i - 1][j]
            if before == curr:
                continue
            elif abs(before - curr) > 1:
                failed = True
                break
            elif before < curr:
                for x in range(1, X+1):
                    if i - x < 0:
                        failed = True
                        break
                    before_x = board[i - x][j]
                    if before_x != before:
                        failed = True
                        break
                    if blocked[i-x]:
                        failed = True
                        break
                    blocked[i-x] = True
                if failed:
                    break
            else:
                for x in range(X):
                    if i + x >= N:
                        failed = True
                        break
                    after_x = board[i + x][j]
                    if after_x != curr:
                        failed = True
                        break
                    if blocked[i+x]:
                        failed = True
                        break
                    blocked[i+x] = True
                if failed:
                    break
        if not failed:
            count += 1

    print(f"#{test_case} {count}")
