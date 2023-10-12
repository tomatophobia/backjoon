import sys

sys.stdin = open('input.txt', 'r')


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


four = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, H, K = map(int, input().rstrip().split(' '))
runner = []
for _ in range(M):
    x, y, d = map(lambda x: int(x) - 1, input().rstrip().split(' '))
    runner.append([x, y, d])
tree_board = [[False] * N for _ in range(N)]  # False 빈공간, True 나무
for _ in range(H):
    x, y = map(lambda x: int(x) - 1, input().rstrip().split(' '))
    tree_board[x][y] = True

cx, cy, cd, goback = N // 2, N // 2, 3, True
catcher_visited = [[False] * N for _ in range(N)]
catcher_visited[cx][cy] = True
score = 0
left_runner = M
for t in range(1, K + 1):
    # 거리 3 이내 도망자 움직임
    runner_board = [[[] for _ in range(N)] for _ in range(N)]
    for x, y, rd in runner:
        if abs(cx - x) + abs(cy - y) > 3:
            runner_board[x][y].append(rd)
            continue
        nx, ny = x + four[rd][0], y + four[rd][1]
        if not is_valid(nx, ny, N):
            rd = (rd + 2) % 4
            nx, ny = x + four[rd][0], y + four[rd][1]
        if [nx, ny] == [cx, cy]:
            nx, ny = x, y
        runner_board[nx][ny].append(rd)
    # 술래 움직임
    if goback:
        cx, cy = cx + four[cd][0], cy + four[cd][1]
        catcher_visited[cx][cy] = True
        ncd = (cd + 1) % 4  # 오른쪽 확인
        ncx, ncy = cx + four[ncd][0], cy + four[ncd][1]
        if catcher_visited[ncx][ncy] == goback:
            ncd = cd
        cd = ncd
        ncx, ncy = cx + four[cd][0], cy + four[cd][1]  # 한바퀴 끝 확인
        if not is_valid(ncx, ncy, N):
            cd = (cd + 2) % 4
            goback = not goback
            catcher_visited[cx][cy] = False
    else:
        cx, cy = cx + four[cd][0], cy + four[cd][1]
        catcher_visited[cx][cy] = False
        ncx, ncy = cx + four[cd][0], cy + four[cd][1]
        if not is_valid(ncx, ncy, N) or not catcher_visited[ncx][ncy]:
            cd = (cd - 1) % 4  # 좌회전
        ncx, ncy = cx + four[cd][0], cy + four[cd][1]  # 한바퀴 끝 확인
        if not catcher_visited[ncx][ncy]:
            cd = (cd - 1) % 4
            goback = not goback
            catcher_visited[cx][cy] = True
    # 도망자 잡기
    for i in range(3):
        x, y = cx + four[cd][0] * i, cy + four[cd][1] * i
        if not is_valid(x, y, N) or tree_board[x][y]:
            continue
        if len(runner_board[x][y]) > 0:
            score += t * len(runner_board[x][y])
            left_runner -= len(runner_board[x][y])
            runner_board[x][y] = []
    # 남은 도망자 없으면 종료
    if left_runner == 0:
        break
    # runner_board -> runner로 다시 변경
    runner = []
    for x in range(N):
        for y in range(N):
            if len(runner_board[x][y]) == 0:
                continue
            for rd in runner_board[x][y]:
                runner.append([x, y, rd])
print(score)

# 1차원 리스트 -> 2차원 리스트 -> 다시 1차원 리스트 -> 2차원 리스트 느낌으로 한 반복문 안에서 유연하게 저장소가 바뀔 수 있다는 것을 잊지 말자.
