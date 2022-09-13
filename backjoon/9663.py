import sys

input = sys.stdin.readline


def fun(board, size, row):
    if row == len(board):
        return 1
    else:
        count = 0
        for col in range(size):
            exist = False
            for i in range(row):
                if board[i] == col or abs(row - i) == abs(board[i] - col):
                    exist = True
                    break

            if not exist:
                board[row] = col
                count += fun(board, size, row + 1)
        return count


n = int(input())
board = [0] * n
print(fun(board, n, 0))

'''
이것도 PyPy3 로만 통과함
2차원 배열 써서 퀸 놓을 수 있는지 체크하면 시간 초과되버림...
'''
