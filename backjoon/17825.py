import sys


def radix_4(n):
    result = ''
    while n > 0:
        a = n % 4
        result = str(a) + result
        n = n // 4
    result = '0' * (10 - len(result)) + result
    return result


input = sys.stdin.readline

dice = list(map(int, input().rstrip().split(' ')))

board = [[i for i in range(0, 41, 2)], [22, 24, 25, 30, 35], [13, 16, 19], [28, 27, 26]]

# 10, 20, 30, 25, 40

max_score = 0
for n in range(4 ** 10):
    four = radix_4(n)
    horse = [(0, 0), (0, 0), (0, 0), (0, 0)]
    score = 0
    error = False
    for i in range(10):
        h = int(four[i])
        if horse[h] is None:
            error = True
            break
        x, y = horse[h]
        d = dice[i]
        if (x, y) == (0, 5):
            d -= 1
            x, y = 2, 0
        elif (x, y) == (0, 10):
            d -= 1
            x, y = 1, 0
        elif (x, y) == (0, 15):
            d -= 1
            x, y = 3, 0
        if d != 0:
            dy = y + d
            if dy >= len(board[x]):
                leftd = dy - len(board[x]) + 1
                if x == 0:
                    horse[h] = None
                    continue
                elif x == 1:
                    if leftd == 1:
                        x, y = 0, len(board[0]) - 1
                    else:
                        horse[h] = None
                        continue
                elif x == 2 or x == 3:
                    if leftd == 5:
                        horse[h] = None
                        continue
                    elif leftd == 4:
                        x, y = 0, len(board[0]) - 1
                    else:
                        x, y = 1, leftd + 1
            else:
                y = dy
        if (x, y) in horse:
            error = True
            break
        score += board[x][y]
        horse[h] = (x, y)
    if error:
        continue
    if score > max_score:
        max_score = score
print(max_score)
