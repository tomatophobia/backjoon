import sys

sys.stdin = open('input.txt', 'r')

lr = [[0, 1], [0, -1]]
ud = [[1, 0], [-1, 0]]
four = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, H, K = map(int, input().rstrip().split(' '))
catcher = [N // 2, N // 2, 3]
catcher_visited = [[False] * N for _ in range(N)]
catcher_visited[catcher[0]][catcher[1]] = True
catcher_way = True
runner = []
for _ in range(M):
    x, y, d = map(int, input().rstrip().split(' '))
    runner.append([x - 1, y - 1, (d - 1)])
tree = [[False] * N for _ in range(N)]
for _ in range(H):
    x, y = map(int, input().rstrip().split(' '))
    tree[x-1][y-1] = True
point = 0
for k in range(1, K + 1):
    # 도망자 움직임
    cx, cy, cd = catcher
    for rr in runner:
        rx, ry, rd = rr
        if abs(cx - rx) + abs(cy - ry) > 3:
            continue
        nx, ny = rx + four[rd][0], ry + four[rd][1]
        if 0 <= nx < N and 0 <= ny < N:
            if [nx, ny] == [cx, cy]:
                continue
        else:
            rd = (rd + 2) % 4
            rr[2] = rd
            nx, ny = rx + four[rd][0], ry + four[rd][1]
            if [nx, ny] == [cx, cy]:
                continue
        rr[0], rr[1] = nx, ny
    # 술래 움직임
    if catcher_way:
        # 정방향
        nx, ny = cx + four[cd][0], cy + four[cd][1]
        if [nx, ny] == [0, 0]:
            nd = (cd + 2) % 4
            catcher_way = False
        else:
            cd_cand = (cd + 1) % 4
            nnx, nny = nx + four[cd_cand][0], ny + four[cd_cand][1]
            if catcher_visited[nnx][nny]:
                cd_cand = cd
            nd = cd_cand
            catcher_visited[nx][ny] = True
        catcher = [nx, ny, nd]
    else:
        # 역방향
        nx, ny = cx + four[cd][0], cy + four[cd][1]
        if [nx, ny] == [N // 2, N // 2]:
            nd = (cd + 2) % 4
            catcher_way = True
        else:
            cd_cand = cd
            nnx, nny = nx + four[cd_cand][0], ny + four[cd_cand][1]
            if nnx < 0 or nnx >= N or nny < 0 or nny >= N or not catcher_visited[nnx][nny]:
                cd_cand = (cd - 1) % 4
            nd = cd_cand
            catcher_visited[nx][ny] = False
        catcher = [nx, ny, nd]
    # 도망자 잡기
    next_runner = []
    cx, cy, cd = catcher
    sight = [[cx, cy], [cx + four[cd][0], cy + four[cd][1]], [cx + four[cd][0] * 2, cy + four[cd][1] * 2]]
    count = 0
    for rx, ry, rd in runner:
        if tree[rx][ry]:
            next_runner.append([rx, ry, rd])
        elif [rx, ry] in sight:
            count += 1
        else:
            next_runner.append([rx, ry, rd])
    runner = next_runner
    point += k * count
    if len(runner) == 0:
        break
print(point)

"""
시간 초과가 나면...
1. while 무한 루프 의심
2. 진짜 느린지 시간 복잡도 생각
3. 1번 문제도 방심하지 말 것
"""
