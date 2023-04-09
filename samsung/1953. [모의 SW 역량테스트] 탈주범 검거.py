from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하, 우, 상, 좌
tunnels = [[], [0, 1, 2, 3], [0, 2], [1, 3], [1, 2], [0, 1], [0, 3], [2, 3]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().rstrip().split(" "))
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split(" "))))

    if L == 1:
        print(f"{test_case} 1")
        continue

    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    count = 1
    queue = deque([[R, C, 1]])
    while len(queue) > 0:
        r, c, t = queue.popleft()
        if t == L:
            continue
        for di in tunnels[board[r][c]]:
            dr, dc = r + dirs[di][0], c + dirs[di][1]
            connected = board[dr][dc] > 0 and (di + 2) % 4 in tunnels[board[dr][dc]]
            if dr < 0 or dr >= N or dc < 0 or dc >= M or not connected or visited[dr][dc]:
                continue
            visited[dr][dc] = True
            count += 1
            queue.append([dr, dc, t + 1])

    print(f"#{test_case} {count}")

    # XXX 아직 안 풀었음

