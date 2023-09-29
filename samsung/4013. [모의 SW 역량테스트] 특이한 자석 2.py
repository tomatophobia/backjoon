import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    magnet = []
    for _ in range(4):
        magnet.append(list(map(int, input().rstrip().split(' '))))
    head = [0, 0, 0, 0]

    for _ in range(K):
        m, d = map(int, input().rstrip().split(' '))
        m = m - 1
        move_candidate = [[m, d]]
        mr = m + 1
        dr = -d
        while mr < 4:
            if magnet[mr - 1][(head[mr - 1] + 2) % 8] == magnet[mr][(head[mr] - 2) % 8]:
                break
            move_candidate.append([mr, dr])
            mr += 1
            dr = -dr
        ml = m - 1
        dl = -d
        while ml >= 0:
            if magnet[ml + 1][(head[ml + 1] - 2) % 8] == magnet[ml][(head[ml] + 2) % 8]:
                break
            move_candidate.append([ml, dl])
            ml -= 1
            dl = -dl
        for mm, dd in move_candidate:
            head[mm] = (head[mm] - dd) % 8
    score = 0
    for i in range(4):
        score += magnet[i][head[i]] * pow(2, i)
    print(f'#{test_case} {score}')
