import sys

input = sys.stdin.readline


def w(a, b, c, d):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        x = d[20][20][20]
        if x:
            return x
        else:
            d[20][20][20] = w(20, 20, 20, d)
            return d[20][20][20]
    elif a < b < c:
        x = d[a][b][c]
        if x:
            return x
        else:
            d[a][b][c] = w(a, b, c - 1, d) + w(a, b - 1, c - 1, d) - w(a, b - 1, c, d)
            return d[a][b][c]
    else:
        x = d[a][b][c]
        if x:
            return x
        else:
            d[a][b][c] = w(a - 1, b, c, d) + w(a - 1, b - 1, c, d) + w(a - 1, b, c - 1, d) - w(a - 1, b - 1, c - 1, d)
            return d[a][b][c]


d = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c, d)}")

'''
제발 출력 형식 잘 읽자...
'''
