import sys

input = sys.stdin.readline

N = int(input().rstrip())
blue = [[False] * 4 for _ in range(6)]
green = [[False] * 4 for _ in range(6)]
score = 0
for _ in range(N):
    t, x, y = map(int, input().rstrip().split(' '))
    for i in range(2):
        blocks = []
        if i == 0:
            # blue
            board = blue
            if t == 1:
                blocks = [(1, 3 - x)]
            elif t == 2:
                blocks = [(1, 3 - x), (0, 3 - x)]
            elif t == 3:
                blocks = [(1, 3 - x), (1, 2 - x)]
        else:
            # green
            board = green
            if t == 1:
                blocks = [(1, y)]
            elif t == 2:
                blocks = [(1, y), (1, y + 1)]
            elif t == 3:
                blocks = [(1, y), (0, y)]
        # move
        while True:
            next_blocks = list(map(lambda p: (p[0] + 1, p[1]), blocks))
            valid = True
            for b in next_blocks:
                if b[0] >= 6 or board[b[0]][b[1]]:
                    valid = False
                    break
            if not valid:
                break
            blocks = next_blocks
        for b in blocks:
            board[b[0]][b[1]] = True
        # erase 1
        dead = []
        for r in range(5, 1, -1):
            full = True
            for c in range(4):
                if not board[r][c]:
                    full = False
            if full:
                dead.append(r)
        for r in dead:
            board.pop(r)
        for _ in range(len(dead)):
            board.insert(0, [False] * 4)
            score += 1
        # erase 2
        dead = []
        for r in range(1, -1, -1):
            exist = False
            for c in range(4):
                if board[r][c]:
                    exist = True
            if exist:
                dead.append(r)
        for _ in range(len(dead)):
            board.pop()
            board.insert(0, [False] * 4)
print(score)
tiles = 0
for r in range(6):
    for c in range(4):
        if blue[r][c]:
            tiles += 1
        if green[r][c]:
            tiles += 1
print(tiles)
