import sys

input = sys.stdin.readline

N, L = map(int, input().rstrip().split(' '))
board = []
for i in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

count = 0
# 행
for t in range(2):
    for i in range(N):
        if t == 0:
            line = board[i][:]
        else:
            line = [board[r][i] for r in range(N)]
        assist = [False] * N
        before = line[0]
        pos = 1
        while pos < N:
            if line[pos] == before:
                pos += 1
                continue
            elif line[pos] == before + 1:
                success = True
                for j in range(pos-1, pos-1-L, -1):
                    if j < 0 or j >= N or line[j] != line[pos-1] or assist[j]:
                        success = False
                        break
                    assist[j] = True
                if success:
                    pos += 1
                    before = line[pos-1]
                    continue
                else:
                    break
            elif line[pos] == before - 1:
                success = True
                for j in range(pos, pos + L):
                    if j < 0 or j >= N or line[j] != line[pos] or assist[j]:
                        success = False
                        break
                    assist[j] = True
                if success:
                    pos += L
                    before = line[pos-1]
                    continue
                else:
                    break
            else:
                break
        if pos == N:
            count += 1
print(count)
