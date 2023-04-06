import sys
sys.stdin = open("input.txt", "r")


def get(cursor, num):
    return (cursor + num) % 8

T = int(input().rstrip())
for test_case in range(1, T + 1):
    K = int(input().rstrip())
    magnets = []
    cursor = [0, 0, 0, 0]
    for _ in range(4):
        magnets.append(list(map(int, input().rstrip().split(" "))))
    for _ in range(K):
        n, d = map(int, input().rstrip().split(" "))
        n -= 1
        d = -d

        if n == 0:
            move = [[0, d]]
            if magnets[0][get(cursor[0], 2)] != magnets[1][get(cursor[1], 6)]:
                move.append([1, -d])
                if magnets[1][get(cursor[1], 2)] != magnets[2][get(cursor[2], 6)]:
                    move.append([2, d])
                    if magnets[2][get(cursor[2], 2)] != magnets[3][get(cursor[3], 6)]:
                        move.append([3, -d])
            for i, dd in move:
                cursor[i] = (cursor[i] + dd) % 8
        elif n == 1:
            move = [[1, d]]
            if magnets[1][get(cursor[1], 6)] != magnets[0][get(cursor[0], 2)]:
                move.append([0, -d])
            if magnets[1][get(cursor[1], 2)] != magnets[2][get(cursor[2], 6)]:
                move.append([2, -d])
                if magnets[2][get(cursor[2], 2)] != magnets[3][get(cursor[3], 6)]:
                    move.append([3, d])
            for i, dd in move:
                cursor[i] = (cursor[i] + dd) % 8
        elif n == 2:
            move = [[2, d]]
            if magnets[2][get(cursor[2], 2)] != magnets[3][get(cursor[3], 6)]:
                move.append([3, -d])
            if magnets[2][get(cursor[2], 6)] != magnets[1][get(cursor[1], 2)]:
                move.append([1, -d])
                if magnets[1][get(cursor[1], 6)] != magnets[0][get(cursor[0], 2)]:
                    move.append([0, d])
            for i, dd in move:
                cursor[i] = (cursor[i] + dd) % 8
        elif n == 3:
            move = [[3, d]]
            if magnets[3][get(cursor[3], 6)] != magnets[2][get(cursor[2], 2)]:
                move.append([2, -d])
                if magnets[2][get(cursor[2], 6)] != magnets[1][get(cursor[1], 2)]:
                    move.append([1, d])
                    if magnets[1][get(cursor[1], 6)] != magnets[0][get(cursor[0], 2)]:
                        move.append([0, -d])
            for i, dd in move:
                cursor[i] = (cursor[i] + dd) % 8
    score = 0
    for i in range(4):
        score += magnets[i][cursor[i]] * (2 ** i)
    print(f"#{test_case} {score}")