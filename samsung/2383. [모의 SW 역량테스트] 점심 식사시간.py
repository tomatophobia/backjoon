from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input().rstrip())
for test_case in range(1, T + 1):
    N = int(input().rstrip())
    people = []
    stairs = []
    for i in range(N):
        line = list(map(int, input().rstrip().split(' ')))
        for j in range(N):
            if line[j] == 1:
                people.append([i, j])
            elif line[j] > 1:
                stairs.append([i, j, line[j]])

    P = len(people)
    min_time = float("inf")
    for p in range(2 ** P):
        arrives = [[0] * (N * 2), [0] * (N * 2)]

        for i in range(P):
            s = p % 2
            sx, sy, _ = stairs[s]
            px, py = people[i]
            d = abs(px - sx) + abs(py - sy)
            arrives[s][d] += 1
            p = p // 2

        max_t = 0
        for a in range(2):
            arrive = arrives[a]
            sx, sy, slen = stairs[a]
            sq = deque([])
            lq = deque([])
            end = 0
            for t in range(len(arrive) + slen):
                if t < len(arrive) and arrive[t] > 0:
                    for _ in range(arrive[t]):
                        lq.append(t)
                while len(sq) > 0 and t - sq[0] >= slen:
                    sq.popleft()
                    end = t
                while len(sq) < 3 and len(lq) > 0 and t - lq[0] >= 1:
                    lq.popleft()
                    sq.append(t)
            if end > max_t:
                max_t = end

        if max_t < min_time:
            min_time = max_t

    print(f"#{test_case} {min_time}")
