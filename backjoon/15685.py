import sys

input = sys.stdin.readline

board = [[False] * 101 for _ in range(101)]
N = int(input())
dragon = []
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in range(N):
    x, y, d, g = map(int, input().rstrip().split(' '))
    dx, dy = directions[d]
    dragon = [(x, y), (x + dx, y + dy)]
    for _ in range(g):
        next = []
        p, q = dragon[-1]
        for i in range(len(dragon) - 2, -1, -1):
            a, b = dragon[i]
            to_a, to_b = a - p, b - q
            c, d = p - to_b, q + to_a
            next.append((c, d))
        dragon += next
    for x, y in dragon:
        board[y][x] = True

count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            count += 1
print(count)
