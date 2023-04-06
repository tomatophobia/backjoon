import sys

sys.stdin = open("input.txt", "r")

dirs = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().rstrip().split(' '))

    aMove = list(map(int, input().rstrip().split(' ')))
    bMove = list(map(int, input().rstrip().split(' ')))
    aPos = [0, 0]
    bPos = [9, 9]

    bcs = []
    for _ in range(A):
        x, y, c, p = map(int, input().rstrip().split(' '))
        bcs.append([y-1, x-1, c, p])

    energy_sum = 0

    for i in range(M + 1):
        # charge
        ax, ay = aPos
        bx, by = bPos
        aCandidate = [[-1, 0]]
        bCandidate = [[-1, 0]]
        for bci in range(len(bcs)):
            x, y, c, p = bcs[bci]
            if abs(ax - x) + abs(ay - y) <= c:
                aCandidate.append([bci, p])
            if abs(bx - x) + abs(by - y) <= c:
                bCandidate.append([bci, p])
        max_energy = 0
        for aBci, aP in aCandidate:
            for bBci, bP in bCandidate:
                energy = 0
                if aBci == bBci:
                    energy = aP // 2 + bP // 2
                else:
                    energy = aP + bP
                if energy > max_energy:
                    max_energy = energy
        energy_sum += max_energy

        if i == M:
            break
        # move
        aPos = [ax + dirs[aMove[i]][0], ay + dirs[aMove[i]][1]]
        bPos = [bx + dirs[bMove[i]][0], by + dirs[bMove[i]][1]]

    print(f"#{test_case} {energy_sum}")
