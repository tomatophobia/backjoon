import sys

sys.stdin = open('input.txt', 'r')

import heapq


class Rabbit:
    def __init__(self, pid, d):
        self.pid = pid
        self.d = d
        self.jumps = 0
        self.x = 0
        self.y = 0
        self.score = 0

    def __lt__(self, other):
        if self.jumps != other.jumps:
            return self.jumps < other.jumps
        elif self.x + self.y != other.x + other.y:
            return self.x + self.y < other.x + other.y
        elif self.x != other.x:
            return self.x < other.x
        elif self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid


four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
Q = int(input().rstrip())
N = 0
M = 0
rabbit_ref = {}  # id -> 토끼
rabbit_queue = []  # (총 점프 횟수, 행 + 열, 행, 열, 고유번호)
shift = 0
for _ in range(Q):
    cmd = list(map(int, input().rstrip().split(' ')))
    if cmd[0] == 100:
        N, M, P = cmd[1], cmd[2], cmd[3]
        for i in range(P):
            pid, d = cmd[4 + 2 * i], cmd[5 + 2 * i]
            rabbit = Rabbit(pid, d)
            rabbit_ref[pid] = rabbit
            heapq.heappush(rabbit_queue, rabbit)
    elif cmd[0] == 200:
        K, S = cmd[1], cmd[2]
        best_rabbit = None
        best_score = [-float('inf'), -float('inf'), -float('inf'), -float('inf')]  # 행 + 열, 행, 열, 고유번호 최대
        for _ in range(K):
            rabbit = heapq.heappop(rabbit_queue)
            bx, by = -1, -1
            best_pos_score = [-float('inf'), -float('inf'), -float('inf')]  # 행 + 열, 행, 열 최대
            for dx, dy in four:
                nx = (rabbit.x + dx * rabbit.d) % (2 * (N - 1))
                nx = nx if 0 <= nx < N else 2 * (N - 1) - nx
                ny = (rabbit.y + dy * rabbit.d) % (2 * (M - 1))
                ny = ny if 0 <= ny < M else 2 * (M - 1) - ny
                pos_score = [nx + ny, nx, ny]
                if pos_score > best_pos_score:
                    bx, by = nx, ny
                    best_pos_score = pos_score
            rabbit.x, rabbit.y = bx, by
            rabbit.score -= bx + by + 2
            shift += bx + by + 2
            rabbit.jumps += 1
            heapq.heappush(rabbit_queue, rabbit)
            round_score = [bx + by, bx, by, rabbit.pid]
            if round_score > best_score:
                best_score = round_score
                best_rabbit = rabbit
        best_rabbit.score += S
    elif cmd[0] == 300:
        pid, L = cmd[1], cmd[2]
        rabbit = rabbit_ref[pid]
        if rabbit is None:
            continue
        rabbit.d *= L
    elif cmd[0] == 400:
        best_score = 0
        for _, rabbit in rabbit_ref.items():
            if rabbit.score > best_score:
                best_score = rabbit.score
        print(best_score + shift)
# 그림에 2차원 보드가 나온다고 꼭 2차원 배열이 필요하진 않다. 문제 잘 읽어보자.
# 토끼가 움직이고 나서 점프 횟수 갱신을 까먹었다. 항상 상태가 바뀔 때 부수효과들이 무엇인지 까먹지 말자... 안까먹을 수 있나? 적어놓을까?
