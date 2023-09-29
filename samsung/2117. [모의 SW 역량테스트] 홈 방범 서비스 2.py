import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().rstrip().split())
    house = []
    for x in range(N):
        l = list(map(int, input().rstrip().split()))
        for y in range(N):
            if l[y] == 1:
                house.append([x, y])
    len_house = len(house)

    max_house = 0
    for x in range(N):
        for y in range(N):
            dist = [0] * (2 * N)
            for hx, hy in house:
                d = abs(hx - x) + abs(hy - y)
                dist[d] += 1
            num_house = len_house
            for d in range(2*N - 1, -1, -1):
                if M * num_house >= pow(d + 1, 2) + pow(d, 2):
                    if max_house < num_house:
                        max_house = num_house
                    break
                num_house = num_house - dist[d]
                if num_house == 0:
                    break
    print(f'#{test_case} {max_house}')
