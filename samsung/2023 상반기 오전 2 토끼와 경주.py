import sys
import time

sys.stdin = open('input.txt', 'r')

import heapq


class Rabbit:
    def __init__(self, pid, dist, jump, location, score):
        self.pid = pid
        self.dist = dist
        self.jump = jump
        self.location = location
        self.score = score


Q = int(input())
N = 0
M = 0
P = 0
pidToNum = {}

rabbits = []
rheap = []  # 적은 점프, 작은 행 + 열, 작은 행, 작은 열, 작은 pid , rabbit
total_shift = 0

for _ in range(Q):
    cmd = list(map(int, input().rstrip().split()))
    if cmd[0] == 100:
        # 초기 설정
        N, M, P = cmd[1], cmd[2], cmd[3]
        for i in range(P):
            pid, di = cmd[4 + i * 2], cmd[4 + i * 2 + 1]
            rb = Rabbit(pid, di, 0, [0, 0], 0)
            rabbits.append(rb)
            heapq.heappush(rheap, (0, 0, 0, 0, pid, rb))
            pidToNum[pid] = i
    elif cmd[0] == 200:
        K, S = cmd[1], cmd[2]
        # 경주 진행
        max_round_rabbit = None
        max_round_rabbit_score = (-1, -1, -1, -1)
        for _ in range(K):
            _, _, _, _, _, rb = heapq.heappop(rheap)  # log(P)
            rb.jump += 1
            max_pos = [-1, -1]
            max_pos_score = (-1, -1, -1)  # 행 + 열, 행, 열
            rx, ry = rb.location
            for ddd in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dx, dy = ddd
                left = rb.dist
                cx, cy = (rx + left * dx) % (2 * (N - 1)), (ry + left * dy) % (2 * (M - 1))
                if cx >= N:
                    cx = 2 * N - cx - 2
                if cy >= M:
                    cy = 2 * M - cy - 2
                if max_pos_score < (cx + cy, cx, cy):
                    max_pos_score = (cx + cy, cx, cy)
                    max_pos = [cx, cy]
            rb.location = max_pos
            sum_max_pos = sum(max_pos)
            rb.score -= sum_max_pos + 2
            total_shift += sum_max_pos + 2
            heapq.heappush(rheap, (rb.jump, sum_max_pos, max_pos[0], max_pos[1], rb.pid, rb))  # log(P)
            if (sum_max_pos, rb.location[0], rb.location[1], rb.pid) > max_round_rabbit_score:
                max_round_rabbit = rb
                max_round_rabbit_score = (sum_max_pos, rb.location[0], rb.location[1], rb.pid)
        max_round_rabbit.score += S
    elif cmd[0] == 300:
        # 점프 거리 변경
        pid, L = cmd[1], cmd[2]
        rb = rabbits[pidToNum[pid]]
        rb.dist *= L
    elif cmd[0] == 400:
        # 최고 토끼 선정, 종료
        max_score = 0
        for rb in rabbits:
            if rb.score > max_score:
                max_score = rb.score
        print(max_score + total_shift)
