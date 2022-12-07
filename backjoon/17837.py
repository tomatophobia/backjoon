import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

horse = [[[] for _ in range(N)] for _ in range(N)]
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
where = []
for i in range(K):
    r, c, d = map(int, input().rstrip().split(' '))
    r -= 1
    c -= 1
    d -= 1
    horse[r][c].append((i, dirs[d]))
    if len(horse[r][c]) >= 4:
        print(0)
        exit(0)
    where.append((r, c))

count = 1
while count < 1000:
    end = False
    for i in range(K):
        r, c = where[i]
        l = horse[r][c]
        start = -1
        for j in range(len(l)):
            if l[j][0] == i:
                start = j
                break
        horse[r][c] = l[:start]
        above = l[start:]
        d = above[0][1]
        dr, dc = r + d[0], c + d[1]
        if dr < 0 or dr >= N or dc < 0 or dc >= N or board[dr][dc] == 2:
            d = (-d[0], -d[1])
            above[0] = (above[0][0], d)
            dr, dc = r + d[0], c + d[1]
            if dr < 0 or dr >= N or dc < 0 or dc >= N or board[dr][dc] == 2:
                dr, dc = r, c
            elif board[dr][dc] == 1:
                above.reverse()
        elif board[dr][dc] == 1:
            above.reverse()
        horse[dr][dc].extend(above)
        if len(horse[dr][dc]) >= 4:
            end = True
            break
        for index, _ in above:
            where[index] = (dr, dc)
    if end:
        break
    count += 1

print(count if count < 1000 else -1)
