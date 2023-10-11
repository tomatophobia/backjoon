import sys

sys.stdin = open('input.txt', 'r')

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

four = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M, K = map(int, input().rstrip().split(' '))
board = []  # [총 여러 개]
for _ in range(N):
    board.append(list(map(lambda x: [int(x)], input().rstrip().split(' '))))
player = []  # [x, y, 방향, 초기능력치, 총]
player_board = [[None] * N for _ in range(N)]  # [방향, 초기능력치, 총]
for _ in range(M):
    x, y, d, s = map(int, input().rstrip().split(' '))
    player.append([x - 1, y - 1, d, s, 0])
    player_board[x-1][y-1] = [d, s, 0]

scores = [0] * M
# board, player, player_board를 갱신해야 한다.
for _ in range(K):
    for pi in range(len(player)):
        px, py, pd, ps, pg = player[pi]
        # 1-1 초기 방향으로 이동
        nd = pd
        nx, ny = px + four[nd][0], py + four[nd][1]
        if not is_valid(nx, ny, N):
            nd = (nd + 2) % 4
            nx, ny = px + four[nd][0], py + four[nd][1]
        player[pi] = [nx, ny, nd, ps, pg]
        player_board[px][py] = None
        # 2 이동 후
        if player_board[nx][ny] is None:
            # 2-1 플레이어가 없는 경우
            guns = board[nx][ny]
            ng = pg
            for gi in range(len(guns)):
                if guns[gi] > ng:
                    guns[gi], ng = ng, guns[gi]
            # 갱신 (board는 반복문으로 갱신됨)
            player[pi][4] = ng
            player_board[nx][ny] = player[pi][2:]
        else:
            # 2-2 플레이어가 있는 경우
            opi = player.index([nx, ny] + player_board[nx][ny])  # O(30)
            ox, oy, od, os, og = player[opi]
            # 2-2-1 결투
            win_i = -1
            loser_i = -1
            if ps + pg > os + og:
                win_i = pi
                loser_i = opi
            elif ps + pg < os + og:
                win_i = opi
                loser_i = pi
            else:
                if ps > os:
                    win_i = pi
                    loser_i = opi
                else:
                    win_i = opi
                    loser_i = pi
            scores[win_i] += abs(ps + pg - os - og)
            # 2-2-2 진 플레이어 총 놓고 이동
            lx, ly, ld, ls, lg = player[loser_i]
            # 총을 안들고 있을 수 있다.
            if lg > 0:
                board[lx][ly].append(lg)
            nlg = 0
            nld = ld
            nlx, nly = lx + four[nld][0], ly + four[nld][1]
            while not is_valid(nlx, nly, N) or player_board[nlx][nly] is not None:
                nld = (nld + 1) % 4
                nlx, nly = lx + four[nld][0], ly + four[nld][1]
            guns = board[nlx][nly]
            for gi in range(len(guns)):
                if guns[gi] > nlg:
                    guns[gi], nlg = nlg, guns[gi]
            player[loser_i] = [nlx, nly, nld, ls, nlg]
            player_board[nlx][nly] = player[loser_i][2:]
            # 2-2-3 이긴 플레이어 공격력 높은 총 획득
            wx, wy, wd, ws, wg = player[win_i]
            guns = board[wx][wy]
            for gi in range(len(guns)):
                if guns[gi] > wg:
                    guns[gi], wg = wg, guns[gi]
            player[win_i][4] = wg
            player_board[wx][wy] = player[win_i][2:]
for s in scores:
    print(s, end=' ')
# 내가 갱신해야 하는 참조, 배열을 잊지 말고 기록하면서 코딩하자.
