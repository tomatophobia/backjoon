import math
import sys
sys.stdin = open("input.txt", "r")

T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, M = map(int, input().rstrip().split(" "))
    houses = []
    for i in range(N):
        line = list(map(int, input().rstrip().split(" ")))
        for j in range(N):
            if line[j] == 1:
                houses.append([i, j])

    K = math.floor((1 + math.sqrt(2 * len(houses) * M - 1)) / 2)

    max_count = 0
    while K > 0:
        cost = K ** 2 + (K - 1) ** 2
        for i in range(N):
            for j in range(N):
                hcount = 0
                for hx, hy in houses:
                    d = abs(hx - i) + abs(hy - j)
                    if d < K:
                        hcount += 1
                if hcount * M >= cost and hcount > max_count:
                    max_count = hcount
        K -= 1

    print(f"#{test_case} {max_count}")
