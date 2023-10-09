import sys

sys.stdin = open('input.txt', 'r')

eight = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
N, M, K = map(int, input().rstrip().split(' '))
atoms = []
for _ in range(M):
    x, y, m, s, d = map(int, input().rstrip().split(' '))
    atoms.append([x - 1, y - 1, m, s, d])

for _ in range(K):
    # 이동
    board = [[[] for _ in range(N)] for _ in range(N)]
    for x, y, m, s, d in atoms:
        nx, ny = (x + eight[d][0] * s) % N, (y + eight[d][1] * s) % N
        board[nx][ny].append([m, s, d])
    # 합성
    next_atoms = []
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) == 0:
                continue
            elif len(board[x][y]) == 1:
                m, s, d = board[x][y][0]
                next_atoms.append([x, y, m, s, d])
            else:
                sum_m = 0
                sum_s = 0
                d_count = 0
                for m, s, d in board[x][y]:
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        d_count += 1
                if sum_m // 5 == 0:
                    continue
                next_d = []
                if d_count == 0 or d_count == len(board[x][y]):
                    next_d = [0, 2, 4, 6]
                else:
                    next_d = [1, 3, 5, 7]
                for d in next_d:
                    next_atoms.append([x, y, sum_m // 5, sum_s // len(board[x][y]), d])
    atoms = next_atoms
sum_mass = 0
for _, _, m, _, _ in atoms:
    sum_mass += m
print(sum_mass)
