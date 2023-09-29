import sys

sys.stdin = open("input.txt", "r")

T = int(input())
four = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
for test_case in range(1, T + 1):
    M, A = map(int, input().rstrip().split(' '))
    ma = list(map(int, input().rstrip().split(' ')))
    mb = list(map(int, input().rstrip().split(' ')))

    chargers = []
    for _ in range(A):
        x, y, c, p = map(int, input().rstrip().split(' '))
        chargers.append([y - 1, x - 1, c, p])

    ax, ay = [0, 0]
    bx, by = [9, 9]
    charge_sum = 0
    # T = 0 일 때 충전
    possible_a = []
    possible_b = []
    for i in range(len(chargers)):
        cx, cy, cc, cp = chargers[i]
        if abs(cx - ax) + abs(cy - ay) <= cc:
            possible_a.append(i)
        if abs(cx - bx) + abs(cy - by) <= cc:
            possible_b.append(i)
    if len(possible_a) > 0 and len(possible_b) > 0:
        max_c = 0
        for ai in possible_a:
            for bi in possible_b:
                c = chargers[ai][3] + chargers[bi][3]
                if ai == bi:
                    c /= 2
                if c > max_c:
                    max_c = c
        charge_sum += max_c
    elif len(possible_b) == 0:
        max_c = 0
        for ai in possible_a:
            if chargers[ai][3] > max_c:
                max_c = chargers[ai][3]
        charge_sum += max_c
    elif len(possible_a) == 0:
        max_c = 0
        for bi in possible_b:
            if chargers[bi][3] > max_c:
                max_c = chargers[bi][3]
        charge_sum += max_c
    for m in range(M):
        ax, ay = ax + four[ma[m]][0], ay + four[ma[m]][1]
        bx, by = bx + four[mb[m]][0], by + four[mb[m]][1]
        possible_a = []
        possible_b = []
        for i in range(len(chargers)):
            cx, cy, cc, cp = chargers[i]
            if abs(cx - ax) + abs(cy - ay) <= cc:
                possible_a.append(i)
            if abs(cx - bx) + abs(cy - by) <= cc:
                possible_b.append(i)
        if len(possible_a) > 0 and len(possible_b) > 0:
            max_c = 0
            for ai in possible_a:
                for bi in possible_b:
                    c = chargers[ai][3] + chargers[bi][3]
                    if ai == bi:
                        c //= 2
                    if c > max_c:
                        max_c = c
            charge_sum += max_c
        elif len(possible_b) == 0:
            max_c = 0
            for ai in possible_a:
                if chargers[ai][3] > max_c:
                    max_c = chargers[ai][3]
            charge_sum += max_c
        elif len(possible_a) == 0:
            max_c = 0
            for bi in possible_b:
                if chargers[bi][3] > max_c:
                    max_c = chargers[bi][3]
            charge_sum += max_c
    print(f'#{test_case} {charge_sum}')
