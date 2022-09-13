import sys

input = sys.stdin.readline

n = int(input())

matrix = []
for i in range(n):
    matrix.append(input().rstrip())

direct = [(1, 0), (0, 1), (0, -1), (-1, 0)]
vil = []
visited = [[False] * n for _ in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '1' and not visited[i][j]:
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
                        if 0 <= x_dx < n and 0 <= y_dy < n and matrix[x_dx][y_dy] == '1' and not visited[x_dx][y_dy]:
                            stack.append((x_dx, y_dy))
            vil.append(count)
vil.sort()
print(len(vil))
for i in vil:
    print(i)
