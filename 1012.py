import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split(' '))
    matrix = [[False] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split(' '))
        matrix[a][b] = True

    direct = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    vil = []
    visited = [[False] * n for _ in range(m)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] and not visited[i][j]:
                count = 0
                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    if not visited[x][y]:
                        visited[x][y] = True
                        count += 1
                        for dx, dy in direct:
                            x_dx = x + dx
                            y_dy = y + dy
                            if 0 <= x_dx < m and 0 <= y_dy < n and matrix[x_dx][y_dy] and not visited[x_dx][y_dy]:
                                stack.append((x_dx, y_dy))
                vil.append(count)
    print(len(vil))
