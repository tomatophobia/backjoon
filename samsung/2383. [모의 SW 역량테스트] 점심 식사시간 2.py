import sys

sys.stdin = open("input.txt", "r")

from itertools import combinations
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    people = []
    stairs = []
    for r in range(N):
        l = list(map(int, input().rstrip().split(' ')))
        for c in range(N):
            if l[c] == 1:
                people.append([r, c])
            elif l[c] > 1:
                stairs.append([r, c, l[c]])

    min_time = float('inf')
    for stair1_num_of_people in range(0, N + 1):
        for ts1 in combinations([i for i in range(len(people))], stair1_num_of_people):
            to_stair1 = []
            to_stair2 = []
            s1x, s1y, s1l = stairs[0]
            s2x, s2y, s2l = stairs[1]
            for pn in range(len(people)):
                px, py = people[pn]
                if pn in ts1:
                    to_stair1.append(abs(s1x - px) + abs(s1y - py))
                else:
                    to_stair2.append(abs(s2x - px) + abs(s2y - py))
            to_stair1.sort(reverse=True)
            to_stair2.sort(reverse=True)

            max_t = 0
            # 계단 1
            t = 0
            stair1_queue = deque([])
            stair1_wait_queue = deque([])
            while len(stair1_queue) > 0 or len(to_stair1) > 0:
                t += 1
                while len(to_stair1) > 0:
                    tt = to_stair1.pop()
                    if t >= tt:
                        # 계단 대기줄 추가
                        stair1_wait_queue.append(t)
                    else:
                        to_stair1.append(tt)
                        break
                # 계단 내려가기
                while len(stair1_queue) > 0:
                    et = stair1_queue.popleft()
                    if t - et < s1l:
                        stair1_queue.appendleft(et)
                        break
                # 계단 대기줄 해소
                while len(stair1_queue) < 3 and len(stair1_wait_queue) > 0:
                    wt = stair1_wait_queue.popleft()
                    stair1_queue.append(max(wt + 1, t))
            if t > max_t:
                max_t = t
            # 계단 2
            t = 0
            stair2_queue = deque([])
            stair2_wait_queue = deque([])
            while len(stair2_queue) > 0 or len(to_stair2) > 0:
                t += 1
                while len(to_stair2) > 0:
                    tt = to_stair2.pop()
                    if t >= tt:
                        # 계단 대기줄 추가
                        stair2_wait_queue.append(t)
                    else:
                        to_stair2.append(tt)
                        break
                # 계단 내려가기
                while len(stair2_queue) > 0:
                    et = stair2_queue.popleft()
                    if t - et < s2l:
                        stair2_queue.appendleft(et)
                        break
                # 계단 대기줄 해소
                while len(stair2_queue) < 3 and len(stair2_wait_queue) > 0:
                    wt = stair2_wait_queue.popleft()
                    stair2_queue.append(max(t, wt + 1))
            if t > max_t:
                max_t = t

            if max_t < min_time:
                min_time = max_t
    print(f'#{test_case} {min_time}')
