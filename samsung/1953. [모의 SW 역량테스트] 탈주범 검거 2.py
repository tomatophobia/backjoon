import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
candidate = [
    [],
    [[1, 0], [0, 1], [-1, 0], [0, -1]],
    [[1, 0], [-1, 0]],
    [[0, -1], [0, 1]],
    [[-1, -0], [0, 1]],
    [[1, 0], [0, 1]],
    [[1, 0], [0, -1]],
    [[-1, 0], [0, -1]]
]
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().rstrip().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split())))

    t = 1
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    count = 1
    queue = deque([[R, C]])
    while len(queue) > 0 and t < L:
        next_queue = []
        while len(queue) > 0:
            cr, cc = queue.pop()
            for dr, dc in candidate[board[cr][cc]]:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] or board[nr][nc] == 0 or [-dr, -dc] not in candidate[board[nr][nc]]:
                    continue
                visited[nr][nc] = True
                count += 1
                next_queue.append([nr, nc])
        queue = deque(next_queue)
        t += 1

    print(f'#{test_case} {count}')
