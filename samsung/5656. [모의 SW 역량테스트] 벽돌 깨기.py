"""
문제가 조금 어이없는데 input() 받고 나서 rstrip()을 안해주면 메모리 뻑남... 그냥 습관처럼 쓰자
"""
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().rstrip().split(' '))
    board = []
    for _ in range(H):
        board.append(list(map(int, input().rstrip().split(' '))))

    origin = [board[i][:] for i in range(0, H)]
    min_count = float("inf")
    for l in range(0, W ** N):
        board = [origin[i][:] for i in range(0, H)]
        for _ in range(N):
            n = l % W
            l = l // W
            start = [-1, n]
            for i in range(0, H):
                if board[i][n] > 0:
                    start = [i, n]
                    break
            if start[0] == -1:
                continue

            queue = deque([start])
            while len(queue) > 0:
                x, y = queue.popleft()
                num = board[x][y]
                board[x][y] = 0
                if num <= 1:
                    continue
                for dx, dy in dirs:
                    for i in range(1, num):
                        ddx = x + dx * i
                        ddy = y + dy * i
                        if 0 <= ddx < H and 0 <= ddy < W:
                            if board[ddx][ddy] <= 1:
                                board[ddx][ddy] = 0
                            else:
                                queue.append([x + dx * i, y + dy * i])

            for i in range(0, W):
                s = H - 1
                t = H - 1
                while t >= 0:
                    if board[t][i] > 0:
                        board[s][i], board[t][i] = board[t][i], board[s][i]
                        s -= 1
                        t -= 1
                    else:
                        t -= 1
        count = 0
        for i in range(0, H):
            for j in range(0, W):
                if board[i][j] > 0:
                    count += 1
        if count < min_count:
            min_count = count
        if min_count == 0:
            break

    print(f"#{test_case} {min_count}")
