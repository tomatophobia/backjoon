import sys

sys.stdin = open('input.txt', 'r')


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


four = [[1, 0], [0, 1], [0, -1], [-1, 0]]
xfour = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
N, M, K, C = map(int, input().rstrip().split(' '))

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

kill = 0
drug = [[0] * N for _ in range(N)]
for m in range(M):
    # 인접한 나무 수만큼 성장 O(N^2)
    for x in range(N):
        for y in range(N):
            if board[x][y] <= 0:
                continue
            count = 0
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, N) and board[nx][ny] > 0:
                    count += 1
            board[x][y] += count
    # 나무 번식 O(N^2)
    next_board = [board[r][:] for r in range(N)]  # copy
    for x in range(N):
        for y in range(N):
            if board[x][y] <= 0:
                continue
            cand = []
            for dx, dy in four:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, N) and board[nx][ny] == 0 and drug[nx][ny] == 0:
                    cand.append([nx, ny])
            if len(cand) > 0:
                sibling = board[x][y] // len(cand)
                for cx, cy in cand:
                    next_board[cx][cy] += sibling
    board = next_board
    # 제초제 O(N^2 * K)
    best_score = 0
    best_target = [[0, 0]]
    for x in range(N):
        for y in range(N):
            if board[x][y] <= 0:
                continue
            score = board[x][y]
            target = [[x, y]]
            for dx, dy in xfour:
                nx, ny = x, y
                for _ in range(K):
                    nx, ny = nx + dx, ny + dy
                    if is_valid(nx, ny, N):
                        target.append([nx, ny])
                        if board[nx][ny] > 0:
                            score += board[nx][ny]
                        else:
                            break
                    else:
                        break
            if score > best_score:
                best_score = score
                best_target = target
    # 제초제 1년 지나서 감소 O(N^2)
    for x in range(N):
        for y in range(N):
            if drug[x][y] > 0:
                drug[x][y] -= 1
    for tx, ty in best_target:
        drug[tx][ty] = C
        if board[tx][ty] > 0:
            kill += board[tx][ty]
            best_score -= board[tx][ty]
            board[tx][ty] = 0
print(kill)

# 실수를 찾아서 고칠 때는 그 논리를 다른 곳에서 똑같이 썼는지 3번 점검해라...!
# 내가 한 실수를 다른 곳에서 또하는 경우가 매우 많다. 종이에 실수한 것을 기록해라.
