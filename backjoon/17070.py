import sys


def check_right(x, y, N, board):
    dx, dy = x, y + 1
    return dx < N and dy < N and board[dx][dy] == 0
def check_down(x, y, N, board):
    dx, dy = x + 1, y
    return dx < N and dy < N and board[dx][dy] == 0
def check_right_down(x, y, N, board):
    dx, dy = x + 1, y + 1
    return check_right(x, y, N, board) and check_down(x, y, N, board) and dx < N and dy < N and board[dx][dy] == 0

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    board.append(line)

stack = [[[0, 1], 0]]
dirs = [[0, 1], [1, 1], [1, 0]]
count = 0
while len(stack) > 0:
    [x, y], h = stack.pop()
    if x == N - 1 and y == N - 1:
        count += 1
        continue
    if h == 0:
        if check_right(x, y, N, board):
            stack.append([[x, y + 1], 0])
        if check_right_down(x, y, N, board):
            stack.append([[x + 1, y + 1], 1])
    elif h == 1:
        if check_right(x, y, N, board):
            stack.append([[x, y + 1], 0])
        if check_down(x, y, N, board):
            stack.append([[x + 1, y], 2])
        if check_right_down(x, y, N, board):
            stack.append([[x + 1, y + 1], 1])
    elif h == 2:
        if check_down(x, y, N, board):
            stack.append([[x + 1, y], 2])
        if check_right_down(x, y, N, board):
            stack.append([[x + 1, y + 1], 1])
print(count)
