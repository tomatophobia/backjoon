import sys


def pprint(b):
    for i in range(len(b)):
        print(b[i])

def is_equal_board(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i] != b[i]:
                return False
    return True


def find_2d_max(x):
    gm = 0
    for i in range(len(x)):
        lm = max(x[i])
        if gm < lm:
            gm = lm
    return gm


input = sys.stdin.readline

N = int(input())

board = []

max_elem = 0
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    m = max(line)
    if max_elem < m:
        max_elem = m
    board.append(line)

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

stack = [(board, 0)]
while len(stack) > 0:
    before, depth = stack.pop()

    if depth >= 5:
        continue

    # 아래로
    after = [l[:] for l in before]
    combined = [[False] * N for _ in range(N)]
    for i in range(N - 2, -1, -1):
        for j in range(N):
            cur = after[i][j]
            if cur == 0:
                continue
            pos = (i, j)
            while True:
                nextPos = (pos[0] + 1, pos[1])
                if nextPos[0] < 0 or nextPos[0] >= N or nextPos[1] < 0 or nextPos[1] >= N:
                    break
                if after[nextPos[0]][nextPos[1]] == 0:
                    pos = nextPos
                elif after[nextPos[0]][nextPos[1]] == cur and not combined[nextPos[0]][nextPos[1]]:
                    combined[nextPos[0]][nextPos[1]] = True
                    pos = nextPos
                    break
                else:
                    break
            if pos == (i, j):
                continue
            else:
                after[i][j] = 0
                after[pos[0]][pos[1]] = cur + after[pos[0]][pos[1]]
    if not is_equal_board(before, after):
        lm = find_2d_max(after)
        if max_elem < lm:
            max_elem = lm
        stack.append((after, depth + 1))

    # 위로
    after = [l[:] for l in before]
    combined = [[False] * N for _ in range(N)]
    for i in range(1, N):
        for j in range(N):
            cur = after[i][j]
            if cur == 0:
                continue
            pos = (i, j)
            while True:
                nextPos = (pos[0] - 1, pos[1])
                if nextPos[0] < 0 or nextPos[0] >= N or nextPos[1] < 0 or nextPos[1] >= N:
                    break
                if after[nextPos[0]][nextPos[1]] == 0:
                    pos = nextPos
                elif after[nextPos[0]][nextPos[1]] == cur and not combined[nextPos[0]][nextPos[1]]:
                    combined[nextPos[0]][nextPos[1]] = True
                    pos = nextPos
                    break
                else:
                    break
            if pos == (i, j):
                continue
            else:
                after[i][j] = 0
                after[pos[0]][pos[1]] = cur + after[pos[0]][pos[1]]
    if not is_equal_board(before, after):
        lm = find_2d_max(after)
        if max_elem < lm:
            max_elem = lm
        stack.append((after, depth + 1))
    # 우로
    after = [l[:] for l in before]
    combined = [[False] * N for _ in range(N)]
    for j in range(N - 2, -1, -1):
        for i in range(N):
            cur = after[i][j]
            if cur == 0:
                continue
            pos = (i, j)
            while True:
                nextPos = (pos[0], pos[1] + 1)
                if nextPos[0] < 0 or nextPos[0] >= N or nextPos[1] < 0 or nextPos[1] >= N:
                    break
                if after[nextPos[0]][nextPos[1]] == 0:
                    pos = nextPos
                elif after[nextPos[0]][nextPos[1]] == cur and not combined[nextPos[0]][nextPos[1]]:
                    combined[nextPos[0]][nextPos[1]] = True
                    pos = nextPos
                    break
                else:
                    break
            if pos == (i, j):
                continue
            else:
                after[i][j] = 0
                after[pos[0]][pos[1]] = cur + after[pos[0]][pos[1]]
    if not is_equal_board(before, after):
        lm = find_2d_max(after)
        if max_elem < lm:
            max_elem = lm
        stack.append((after, depth + 1))
    # 좌로
    after = [l[:] for l in before]
    combined = [[False] * N for _ in range(N)]
    for j in range(1, N):
        for i in range(N):
            cur = after[i][j]
            if cur == 0:
                continue
            pos = (i, j)
            while True:
                nextPos = (pos[0], pos[1] - 1)
                if nextPos[0] < 0 or nextPos[0] >= N or nextPos[1] < 0 or nextPos[1] >= N:
                    break
                if after[nextPos[0]][nextPos[1]] == 0:
                    pos = nextPos
                elif after[nextPos[0]][nextPos[1]] == cur and not combined[nextPos[0]][nextPos[1]]:
                    combined[nextPos[0]][nextPos[1]] = True
                    pos = nextPos
                    break
                else:
                    break
            if pos == (i, j):
                continue
            else:
                after[i][j] = 0
                after[pos[0]][pos[1]] = cur + after[pos[0]][pos[1]]
    if not is_equal_board(before, after):
        lm = find_2d_max(after)
        if max_elem < lm:
            max_elem = lm
        stack.append((after, depth + 1))
print(max_elem)
