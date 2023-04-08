from itertools import combinations

import sys
sys.stdin = open("input.txt", "r")


def check_film(film, D, W, K):
    all_good = True
    for w in range(W):
        cur = film[0][w]
        same = 1
        good = False
        for d in range(1, D):
            if cur == film[d][w]:
                same += 1
            else:
                cur = film[d][w]
                same = 1
            if same == K:
                good = True
                break
        if not good:
            all_good = False
            break
    return all_good


T = int(input().rstrip())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().rstrip().split(" "))
    film = []
    for _ in range(D):
        film.append(list(map(int, input().rstrip().split(" "))))

    if K == 1:
        print(f"#{test_case} 0")
        continue

    all_good = check_film(film, D, W, K)
    if all_good:
        print(f"#{test_case} 0")
        continue

    found = K
    for i in range(1, K):
        combs = combinations(range(D), i)
        for comb in combs:
            for binary in range(2 ** i):
                cur_film = [film[ii][:] for ii in range(D)]
                for c in comb:
                    b = binary % 2
                    cur_film[c] = [b] * W
                    binary = binary // 2
                all_good = check_film(cur_film, D, W, K)
                if all_good:
                    found = i
                    break
            if found < K:
                break
        if found < K:
            break

    print(f"#{test_case} {found}")
