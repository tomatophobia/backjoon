import sys
import heapq

sys.stdin = open("input.txt", "r")

T = int(input())
four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input()))))

    dist = [[float('inf')] * N for _ in range(N)]

    dist[0][0] = 0
    heap = [[0, [0, 0]]]
    while len(heap) > 0:
        cd, [cx, cy] = heapq.heappop(heap)
        if cd > dist[cx][cy]:
            continue
        for dx, dy in four:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_d = cd + board[nx][ny]
                if new_d < dist[nx][ny]:
                    dist[nx][ny] = new_d
                    heapq.heappush(heap, [new_d, [nx, ny]])

    print(f'#{test_case} {dist[N - 1][N - 1]}')
