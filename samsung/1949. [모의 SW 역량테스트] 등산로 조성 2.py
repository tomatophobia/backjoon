import sys
sys.stdin = open("input.txt", "r")

T = int(input())
four = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for test_case in range(1, T + 1):
    N, K = map(int, input().rstrip().split(' '))
    board = []
    max_bong = []
    max_height = 0
    for x in range(N):
        l = list(map(int, input().rstrip().split()))
        for y in range(N):
            if l[y] > max_height:
                max_height = l[y]
                max_bong = [[x, y]]
            elif l[y] == max_height:
                max_bong.append([x, y])
        board.append(l)

    max_line = 1
    # K = 0
    for sx, sy in max_bong:
        stack = [[sx, sy, 1]]
        while len(stack) > 0:
            cx, cy, cl = stack.pop()
            for dx, dy in four:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < N and board[cx][cy] > board[nx][ny]:
                    stack.append([nx, ny, cl + 1])
                    if cl + 1 > max_line:
                        max_line = cl + 1


    for k in range(1, K + 1):
        for kx in range(N):
            for ky in range(N):
                board[kx][ky] -= k

                for sx, sy in filter(lambda p: p != [kx, ky], max_bong):
                    stack = [[sx, sy, 1]]
                    while len(stack) > 0:
                        cx, cy, cl = stack.pop()
                        for dx, dy in four:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < N and 0 <= ny < N and board[cx][cy] > board[nx][ny]:
                                stack.append([nx, ny, cl + 1])
                                if cl + 1 > max_line:
                                    max_line = cl + 1

                board[kx][ky] += k

    print(f'#{test_case} {max_line}')

