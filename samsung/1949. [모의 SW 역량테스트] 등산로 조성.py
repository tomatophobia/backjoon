from collections import deque
import sys

sys.stdin = open("input.txt", "r")


def max_road(board, N, high):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    max_depth = 0
    for hx, hy in high:
        # bfs
        visited = [[False] * N for _ in range(N)]
        visited[hx][hy] = True
        queue = deque([[hx, hy, board[hx][hy], 1, visited]])
        while len(queue) > 0:
            x, y, h, d, v = queue.popleft()
            if d > max_depth:
                max_depth = d
            for di in dirs:
                dx, dy = x + di[0], y + di[1]
                if dx < 0 or dx >= N or dy < 0 or dy >= N or board[dx][dy] >= h or v[dx][dy]:
                    continue
                next_v = [v[iii][:] for iii in range(N)]
                next_v[dx][dy] = True
                queue.append([dx, dy, board[dx][dy], d + 1, next_v])
    return max_depth


T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, K = map(int, input().rstrip().split(" "))
    board = []
    for i in range(N):
        board.append(list(map(int, input().rstrip().split(" "))))

    max_height = 0
    high = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > max_height:
                max_height = board[i][j]
                high = [[i, j]]
            elif board[i][j] == max_height:
                high.append([i, j])

    all_max_depth = 0
    for k in range(K + 1):
        if k == 0:
            md = max_road(board, N, high)
            if md > all_max_depth:
                all_max_depth = md
            continue
        for i in range(N):
            for j in range(N):
                cur_board = [board[ii][:] for ii in range(N)]
                cur_board[i][j] -= k
                md = max_road(cur_board, N, high)
                if md > all_max_depth:
                    all_max_depth = md
    print(f"#{test_case} {all_max_depth}")
