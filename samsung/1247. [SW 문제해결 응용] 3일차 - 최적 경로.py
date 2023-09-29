import sys

sys.stdin = open("input.txt", "r")

from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    l = list(map(int, input().rstrip().split()))
    sx, sy = l[:2]
    ex, ey = l[2:4]
    customer = []
    for i in range(N):
        customer.append(l[4 + 2 * i: 4 + 2 * i + 2])

    D = [[float('inf')] * (2 ** N) for _ in range(N)]  # D(s, A) = s에서 시작 A 집합 경유하여 end로 도착, 집합은 bit로 표현
    for s in range(N):
        # D(s, {}) = d(s, end)
        cx, cy = customer[s]
        D[s][0] = abs(cx - ex) + abs(cy - ey)
    for num_a in range(1, N):
        for selected in combinations([i for i in range(N)], num_a):
            selected_bit = 0
            for ss in selected:
                selected_bit |= 2 ** ss
            for s in range(N):
                if s in selected:
                    continue
                cx, cy = customer[s]
                # D(s, A) = A에 속하는 모든 r에 대해 d(s, r) + D(r, A - {r}) 의 최솟값
                for ss in selected:
                    ccx, ccy = customer[ss]
                    new_dist = abs(cx - ccx) + abs(cy - ccy) + D[ss][selected_bit - 2 ** ss]
                    if new_dist < D[s][selected_bit]:
                        D[s][selected_bit] = new_dist
    # 최소 거리 = {1...N} 에 속하는 n에 대해 d(start, n) + D(n, {1...N} - {n})의 최솟값
    min_dist = float('inf')
    for s in range(N):
        cx, cy = customer[s]
        new_dist = abs(sx - cx) + abs(sy - cy) + D[s][2**N - 1 - 2**s]
        if new_dist < min_dist:
            min_dist = new_dist
    print(f'#{test_case} {min_dist}')

