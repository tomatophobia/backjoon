import sys
sys.stdin = open('input.txt', 'r')

four = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M, K = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(lambda gun: [int(gun)], input().rstrip().split())))

player = []
for _ in range(M):
    x, y, d, s = map(int, input().rstrip().split())
    player.append([x - 1, y - 1, d, s, 0, 0])

for _ in range(K):

    for me in player:
        px, py, pd, _, _, _ = me
        # 1-1 움직임
        nx, ny = px + four[pd][0], py + four[pd][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            pd = (pd + 2) % 4
            nx, ny = px + four[pd][0], py + four[pd][1]
        me[0], me[1], me[2] = nx, ny, pd

        # 2 플레이어 있는지 확인
        fighter = []
        for other in player:
            if me[:2] == other[:2] and me[3] != other[3]:
                fighter = other
                break
        if len(fighter) == 0:
            # 2-1 플레이어 없으면 총 교체
            cur_guns = board[me[0]][me[1]]
            if len(cur_guns) > 0:
                max_gun_atk = max(cur_guns)
                if max_gun_atk > me[4]:
                    maxidx = cur_guns.index(max_gun_atk)
                    if me[4] == 0:
                        cur_guns.remove(max_gun_atk)
                    else:
                        cur_guns[maxidx] = me[4]
                    me[4] = max_gun_atk
        else:
            # 2-2 플레이어 있다
            # 2-2-1 싸움
            winner = []
            loser = []
            if me[3] + me[4] > fighter[3] + fighter[4]:
                winner = me
                loser = fighter
            elif me[3] + me[4] < fighter[3] + fighter[4]:
                winner = fighter
                loser = me
            else:
                if me[3] > fighter[3]:
                    winner = me
                    loser = fighter
                elif me[3] < fighter[3]:
                    winner = fighter
                    loser = me
            winner[5] += winner[3] + winner[4] - (loser[3] + loser[4])
            # 2-2-2 진 플레이어 이동
            # 총 내려놓고
            if loser[4] > 0:
                board[loser[0]][loser[1]].append(loser[4])
            loser[4] = 0
            # 이동
            tryd = loser[2]
            while True:
                nx, ny = loser[0] + four[tryd][0], loser[1] + four[tryd][1]
                # 사람 존재하거나 격자 밖
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    tryd = (tryd + 1) % 4
                    continue
                exist = False
                for ppx, ppy, _, pps, _, _ in player:
                    if [ppx, ppy] == [nx, ny] and pps != loser[3]:
                        exist = True
                if exist:
                    tryd = (tryd + 1) % 4
                    continue
                loser[0], loser[1], loser[2] = nx, ny, tryd
                break
            # 총 변경
            cur_guns = board[loser[0]][loser[1]]
            if len(cur_guns) > 0:
                max_gun_atk = max(cur_guns)
                if max_gun_atk > loser[4]:
                    maxidx = cur_guns.index(max_gun_atk)
                    if loser[4] == 0:
                        cur_guns.remove(max_gun_atk)
                    else:
                        cur_guns[maxidx] = loser[4]
                    loser[4] = max_gun_atk
            # 2-2-3 이긴 사람 총 변경
            cur_guns = board[winner[0]][winner[1]]
            if len(cur_guns) > 0:
                max_gun_atk = max(cur_guns)
                if max_gun_atk > winner[4]:
                    maxidx = cur_guns.index(max_gun_atk)
                    if winner[4] == 0:
                        cur_guns.remove(max_gun_atk)
                    else:
                        cur_guns[maxidx] = winner[4]
                    winner[4] = max_gun_atk
for _, _, _, _, _, point in player:
    print(point, end=" ")

# 시뮬레이션 문제 풀 때 그냥 클래스 쓸까? 잔 실수가 너무 많다.
