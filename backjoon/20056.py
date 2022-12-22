import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(' '))

board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = list(map(int, input().rstrip().split(' ')))
    r -= 1
    c -= 1
    board[r][c].append([m, s, d])

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(K):
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    # 이동
    for x in range(N):
        for y in range(N):
            for m, s, d in board[x][y]:
                dx, dy = (x + s * dirs[d][0]) % N, (y + s * dirs[d][1]) % N
                new_board[dx][dy].append([m, s, d])
    # 충돌
    for x in range(N):
        for y in range(N):
            if len(new_board[x][y]) > 1:
                tm = 0
                ts = 0
                oddity = None
                all = True
                for m, s, d in new_board[x][y]:
                    tm += m
                    ts += s
                    if oddity is None:
                        oddity = d % 2 == 1
                    else:
                        if oddity != (d % 2 == 1):
                            all = False
                nm = tm // 5
                ns = ts // len(new_board[x][y])
                if nm > 0:
                    if all:
                        new_board[x][y] = [[nm, ns, 0], [nm, ns, 2], [nm, ns, 4], [nm, ns, 6]]
                    else:
                        new_board[x][y] = [[nm, ns, 1], [nm, ns, 3], [nm, ns, 5], [nm, ns, 7]]
                else:
                    new_board[x][y] = []
    board = new_board
count = 0
for x in range(N):
    for y in range(N):
        count += sum(map(lambda l: l[0], board[x][y]))
print(count)
