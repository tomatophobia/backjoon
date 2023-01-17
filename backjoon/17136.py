import sys


def copy_2d(ll):
    return [ll[i][:] for i in range(len(ll))]


def f(board, side, papers, curr_min):
    # print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))
    # print(side, papers)
    if side == 0:
        return float('inf')

    all_zero = True
    for r in range(10):
        for c in range(10):
            if board[r][c] == 1:
                all_zero = False
                break
        if not all_zero:
            break
    if all_zero:
        return 0

    if curr_min == 0:
        return float('inf')

    min_num = curr_min
    # side used
    if papers[5 - side] > 0:
        for r in range(10):
            for c in range(10):
                if r + side > 10 or c + side > 10:
                    continue
                possible = True
                for i in range(r, r + side):
                    for j in range(c, c + side):
                        if board[i][j] == 0:
                            possible = False
                            break
                    if not possible:
                        break
                if not possible:
                    continue
                next_board = copy_2d(board)
                for i in range(r, r + side):
                    for j in range(c, c + side):
                        next_board[i][j] = 0
                next_papers = papers[:]
                next_papers[5 - side] -= 1
                num = 1 + f(next_board, side, next_papers, min_num - 1)
                if num < min_num:
                    min_num = num
    # side not used
    num = f(board, side - 1, papers, min_num)
    if num < min_num:
        min_num = num
    return min_num


# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

origin = []
for _ in range(10):
    line = list(map(int, input().rstrip().split(' ')))
    origin.append(line)

result = f(copy_2d(origin), 5, [5, 5, 5, 5, 5], float('inf'))

if result == float('inf'):
    print(-1)
else:
    print(result)
