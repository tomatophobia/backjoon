import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
r, c, d = map(int, input().rstrip().split(' '))
board = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

cleaned = [[False] * M for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0
mode = 1
failed = 0
while True:
    if mode == 1:
        if not cleaned[r][c]:
            cleaned[r][c] = True
            count += 1
        mode = 2
    elif mode == 2:
        ld = directions[(d + 3) % 4]
        lr, lc = r + ld[0], c + ld[1]
        if board[lr][lc] == 0 and not cleaned[lr][lc]:
            d = (d + 3) % 4
            r, c = lr, lc
            failed = 0
            mode = 1
        else:
            if failed == 4:
                bd = directions[(d + 2) % 4]
                br, bc = r + bd[0], c + bd[1]
                if board[br][bc] == 0:
                    r, c = br, bc
                    failed = 0
                    mode = 2
                else:
                    break
            else:
                d = (d + 3) % 4
                failed += 1
                mode = 2
print(count)

