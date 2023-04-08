from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dirs = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N = int(input().rstrip())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split(" "))))

    max_path = -1
    for r in range(N - 2):
        for c in range(1, N - 1):
            queue = deque([[r, c, 0, r, c, [board[r][c]]]])  # cur, direction, start, path
            while len(queue) > 0:
                x, y, d, sx, sy, path = queue.popleft()
                if len(path) > 3 and (x, y) == (sx, sy):
                    if len(path) > max_path:
                        max_path = len(path) - 1
                    continue

                next_dirs = [d]
                if len(path) == 1 or d != 0:
                    next_dirs.append((d + 1) % 4)
                for nd in next_dirs:
                    dx, dy = x + dirs[nd][0], y + dirs[nd][1]
                    if (dx, dy) != (sx, sy) and (dx < 0 or dx >= N or dy < 0 or dy >= N or board[dx][dy] in path):
                        continue
                    next_path = path[:]
                    next_path.append(board[dx][dy])
                    queue.append([dx, dy, nd, sx, sy, next_path])

    print(f"#{test_case} {max_path}")
