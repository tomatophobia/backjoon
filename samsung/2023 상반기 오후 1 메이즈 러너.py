import sys

sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().rstrip().split(' '))
temp = [[0] * N for _ in range(N)]
temp2 = [[0] * N for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
people = []
for _ in range(M):
    x, y = map(int, input().rstrip().split())
    people.append([x - 1, y - 1])
ex, ey = map(int, input().rstrip().split())
ex, ey = ex - 1, ey - 1

total_move = 0
for _ in range(K):
    # 참가자 이동
    next_people = []
    for px, py in people:
        cur_dist = abs(ex - px) + abs(ey - py)
        find = []
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = px + dx, py + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and cur_dist > abs(ex - nx) + abs(ey - ny):
                find = [nx, ny]
                break
        if len(find) > 0:
            total_move += 1
            if find != [ex, ey]:
                next_people.append(find)
        else:
            next_people.append([px, py])
    people = next_people
    if len(people) == 0:
        break
    # 정사각형 찾기
    min_p = []
    lu, rd = [float('inf'), float('inf')], [float('inf'), float('inf')]
    min_p_score = float('inf')
    for px, py in people:
        score = max(abs(ex - px), abs(ey - py))
        if min_p_score > score:
            min_p_score = score
            rd = [max(px, ex), max(py, ey)]
            lu = [rd[0] - min_p_score, rd[1] - min_p_score]
            if lu[0] < 0:
                rd[0] += -lu[0]
                lu[0] += -lu[0]
            elif lu[1] < 0:
                rd[1] += -lu[1]
                lu[1] += -lu[1]
        elif min_p_score == score:
            prd = [max(px, ex), max(py, ey)]
            plu = [prd[0] - min_p_score, prd[1] - min_p_score]
            if plu[0] < 0:
                prd[0] += -plu[0]
                plu[0] += -plu[0]
            elif plu[1] < 0:
                prd[1] += -plu[1]
                plu[1] += -plu[1]
            if plu < lu:
                rd = prd
                lu = plu
    # 미로 90도 회전
    # 평행이동
    for rx in range(lu[0], rd[0] + 1):
        for ry in range(lu[1], rd[1] + 1):
            if board[rx][ry] > 0:
                temp[rx - lu[0]][ry - lu[1]] = board[rx][ry] - 1
            else:
                temp[rx - lu[0]][ry - lu[1]] = board[rx][ry]
    # 90도 회전
    for rx in range(min_p_score + 1):
        for ry in range(min_p_score + 1):
            temp2[ry][-rx + min_p_score] = temp[rx][ry]
    # 평행이동
    for rx in range(min_p_score + 1):
        for ry in range(min_p_score + 1):
            board[rx + lu[0]][ry + lu[1]] = temp2[rx][ry]
    # 출구 90도 회전
    ex, ey = ex - lu[0], ey - lu[1]
    ex, ey = ey, -ex + min_p_score
    ex, ey = ex + lu[0], ey + lu[1]
    # 사람 90도 회전
    for pp in range(len(people)):
        px, py = people[pp]
        if lu[0] <= px <= rd[0] and lu[1] <= py <= rd[1]:
            px, py = px - lu[0], py - lu[1]
            px, py = py, -px + min_p_score
            px, py = px + lu[0], py + lu[1]
            people[pp] = [px, py]

print(total_move)
print(ex + 1, ey + 1)

# 가변인 변수와 불변인 변수를 구별해서 사용하기. 나도 모르게 값이 바뀌지 않는지 인지하기
