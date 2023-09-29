import sys

sys.stdin = open("input.txt", "r")


# (x, y) => (y, -x) : 시계 회전
def tracking(r, c, dr, dc, path, sr, sc):
    nr1, nc1 = r + dr, c + dc
    if [nr1, nc1] == [sr, sc]:
        return len(path)
    cand1 = -1
    if 0 <= nr1 < N and 0 <= nc1 < N and board[nr1][nc1] not in path:
        cand1 = tracking(nr1, nc1, dr, dc, path + [board[nr1][nc1]], sr, sc)
    if [dr, dc] == [-1, 1]:
        return cand1
    nr2, nc2 = r + dc, c - dr
    if [nr2, nc2] == [sr, sc]:
        return len(path)
    cand2 = -1
    if 0 <= nr2 < N and 0 <= nc2 < N and board[nr2][nc2] not in path:
        cand2 = tracking(nr2, nc2, dc, -dr, path + [board[nr2][nc2]], sr, sc)
    return max(cand1, cand2)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split())))

    max_count = -1
    end = False
    for r in range(N):
        for c in range(N):
            if r + 1 >= N or c + 1 >= N or c - 1 < 0 or board[r][c] == board[r + 1][c + 1]:
                continue
            count = tracking(r + 1, c + 1, 1, 1, [board[r][c], board[r + 1][c + 1]], r, c)
            if count > max_count:
                max_count = count
                if max_count == 2 * (N - 1):
                    end = True
                    break
        if end:
            break
    print(f'#{test_case} {max_count}')
