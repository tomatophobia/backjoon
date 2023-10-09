import sys

sys.stdin = open('input.txt', 'r')


def print_board(board):
    print('---')
    for i in range(4):
        for j in range(4):
            if board[i][j] is None:
                print(f"{i}, {j},   x, x", end='|')
            else:
                print(f"{board[i][j].x}, {board[i][j].y}, {board[i][j].p:3}, {board[i][j].d}", end='|')
        print('')

class Thief:
    def __init__(self, x, y, p, d):
        self.x = x
        self.y = y
        self.p = p
        self.d = d


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def copy_board(board):
    copied = []
    copied_thieves = [None] * 17
    for i in range(4):
        one_line = []
        for j in range(4):
            if board[i][j] is None:
                one_line.append(None)
            else:
                th = board[i][j]
                new_th = Thief(th.x, th.y, th.p, th.d)
                one_line.append(new_th)
                copied_thieves[th.p] = new_th
        copied.append(one_line)
    return copied, copied_thieves


def dfs(sx, sy, sd, thieves, board):
    # 도둑 이동
    for th in thieves:
        if th is None:
            continue
        nd = th.d
        nx, ny = th.x + eight[nd][0], th.y + eight[nd][1]
        count = 0
        while (not is_valid(nx, ny, 4) or [nx, ny] == [sx, sy]) and count < 8:
            nd = (nd + 1) % 8
            nx, ny = th.x + eight[nd][0], th.y + eight[nd][1]
            count += 1
        if count == 8:  # 움직이지 않음
            continue
        other = board[nx][ny]
        if other is not None:
            other.x, other.y = th.x, th.y
        board[th.x][th.y], board[nx][ny] = board[nx][ny], board[th.x][th.y]
        th.x, th.y, th.d = nx, ny, nd
    # 술래 말 이동
    nx, ny = sx + eight[sd][0], sy + eight[sd][1]
    max_score = 0
    while is_valid(nx, ny, 4):
        copied_board, copied_thieves = copy_board(board)
        thiefxy = copied_board[nx][ny]
        if thiefxy is not None:
            copied_thieves[thiefxy.p] = None
            copied_board[nx][ny] = None
            score = thiefxy.p + dfs(nx, ny, thiefxy.d, copied_thieves, copied_board)
            if max_score < score:
                max_score = score
        nx, ny = nx + eight[sd][0], ny + eight[sd][1]
    return max_score


# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
eight = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = []
thieves = [None] * 17
for x in range(4):
    ll = list(map(int, input().rstrip().split(' ')))
    lll = []
    for y in range(4):
        p, d = ll[2 * y], ll[2 * y + 1]
        thief = Thief(x, y, p, d - 1)
        lll.append(thief)
        thieves[p] = thief
    board.append(lll)

# 술래 세팅
thief0 = board[0][0]
thieves[thief0.p] = None
board[0][0] = None
sx, sy, sd = 0, 0, thief0.d
score = thief0.p + dfs(sx, sy, sd, thieves, board)
print(score)

# 백트래킹 생각보다 어렵지 않다. 겁먹지 말고 재귀 함수를 써도 된다.
# 단 복사할 때 조심하자. board와 thieves가 연결된 데이터인데 복사하다 연결이 끊어져서 고생했다. 클래스 쓸 때는 참조를 잘 관리하는지 생각하자.
