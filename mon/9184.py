table = [[[None for k in range(21)] for j in range(21)] for i in range(21)]
table[0][0][0] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if table[20][20][20] is None:
            table[20][20][20] = w(20, 20, 20)
        return table[20][20][20]

    if a < b and b < c:
        if table[a][b][c] is None:
            table[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return table[a][b][c]
    else:
        if table[a][b][c] is None:
            table[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return table[a][b][c]


if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split(' '))
        if a == b == c == -1:
            break

        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
