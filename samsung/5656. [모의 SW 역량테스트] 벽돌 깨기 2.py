import sys

sys.stdin = open("input.txt", "r")

from collections import deque


def make_try(t, n, w):
    l = []
    while t > 0:
        l.append(t % w)
        t = t // w
    for _ in range(n - len(l)):
        l.append(0)
    return l


T = int(input())
four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for test_case in range(1, T + 1):
    N, W, H = map(int, input().rstrip().split(' '))
    board = []
    for _ in range(H):
        board.append(list(map(int, input().rstrip().split(' '))))

    global_sum = float('inf')
    for tri in range(pow(W, N)):
        cur_board = [board[i][:] for i in range(H)]
        tries = make_try(tri, N, W)
        for t in tries:
            # 첫 번째 부딪침
            fh = 0
            bomb = 0
            for h in range(H):
                if cur_board[h][t] != 0:
                    fh = h
                    bomb = cur_board[h][t]
                    break

            # 연쇄 폭발
            queue = deque([[fh, t, bomb]])
            while len(queue) > 0:
                x, y, b = queue.popleft()
                cur_board[x][y] = 0
                if b > 1:
                    for b in range(1, b):
                        for dx, dy in four:
                            ddx = x + dx * b
                            ddy = y + dy * b
                            if 0 <= ddx < H and 0 <= ddy < W:
                                if cur_board[ddx][ddy] > 1:
                                    queue.append([ddx, ddy, cur_board[ddx][ddy]])
                                cur_board[ddx][ddy] = 0

            # 빈 공간 채우기
            # for w in range(W):
            #     for h in range(H-1, -1, -1):
            #         if cur_board[h][w] == 0:
            #             find = False
            #             for nh in range(h-1, -1, -1):
            #                 if cur_board[nh][w] != 0:
            #                     cur_board[h][w], cur_board[nh][w] = cur_board[nh][w], cur_board[h][w]
            #                     find = True
            #                     break
            #             if not find:
            #                 break
            for jj in range(W):
                replace = []
                for ii in range(0, H):
                    if cur_board[ii][jj] != 0:
                        replace.append(cur_board[ii][jj])
                replace = [0] * (H - len(replace)) + replace
                for ii in range(0, H):
                    cur_board[ii][jj] = replace[ii]

        num_sum = 0
        for h in range(H):
            for w in range(W):
                if cur_board[h][w] == 0:
                    continue
                num_sum += 1
        if num_sum < global_sum:
            global_sum = num_sum
    print(f'#{test_case} {global_sum}')
