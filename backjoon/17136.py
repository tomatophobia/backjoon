import sys


def copy_2d(ll):
    return [ll[i][:] for i in range(len(ll))]

def dfs(x, y, count, board, papers):
    found = False
    while x < 10:
        while y < 10:
            if board[x][y] == 1:
                found = True
                break
            y+=1
        if found:
            break
        y = 0
        x += 1
    if not found:
        return count

    min_count = float('inf')
    for side in range(5, 0, -1):
        if x + side > 10 or y + side > 10 or papers[side - 1] <= 0:
            continue
        possible = True
        for r in range(x, x + side):
            for c in range(y, y + side):
                if board[r][c] == 0:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            continue
        next_board = copy_2d(board)
        for r in range(x, x + side):
            for c in range(y, y + side):
                next_board[r][c] = 0
        next_papers = papers[:]
        next_papers[side - 1] -= 1
        cur_count = dfs(x, y, count + 1, next_board, next_papers)
        if cur_count < min_count:
            min_count = cur_count
    return min_count


# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

origin = []
for _ in range(10):
    line = list(map(int, input().rstrip().split(' ')))
    origin.append(line)

result = dfs(0, 0, 0, origin, [5, 5, 5, 5, 5])
if result == float('inf'):
    print(-1)
else:
    print(result)
