import sys
sys.stdin = open("input.txt", "r")

lr = [[0, 1], [0, -1]]
for _ in range(10):
    test_case = int(input())

    board = []
    start = []
    for x in range(100):
        l = list(map(int, input().rstrip().split(' ')))
        board.append(l)
        if x == 99:
            start = [x, l.index(2)]

    x, y = start
    while x > 0:
        up = True
        for dx, dy in lr:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 100 and 0 <= ny < 100 and board[nx][ny] == 1:
                up = False
                x, y = nx, ny
                nx, ny = x + dx, y + dy
            if not up:
                break
        x, y = x - 1, y


    print(f'#{test_case} {y}')
