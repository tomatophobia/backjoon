import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cube = [[[None] * 3 for _ in range(3)] for _ in range(3)]
    cube[0][0][1] = [['w'] * 3 for _ in range(3)]  # up
    cube[0][0][-1] = [['y'] * 3 for _ in range(3)]  # down
    cube[0][-1][0] = [['r'] * 3 for _ in range(3)]  # front
    cube[0][1][0] = [['o'] * 3 for _ in range(3)]  # back
    cube[-1][0][0] = [['g'] * 3 for _ in range(3)]  # left
    cube[1][0][0] = [['b'] * 3 for _ in range(3)]  # right
    n = int(input())
    commands = input().rstrip(' ').split(' ')
    for cmd in commands:
        if cmd[0] == 'U':
            cur = cube[0][0][1]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][1][0]  # 2행
            left = cube[-1][0][0]  # 0행
            right = cube[1][0][0]  # 0행
            down = cube[0][-1][0]  # 0행
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[0][2], right[0][1], right[0][0], down[0][2], down[0][1], down[0][0], left[0][2], left[0][1], left[0][0], up[2][0], up[2][1], up[2][2] = \
                    up[2][0], up[2][1], up[2][2], right[0][2], right[0][1], right[0][0], down[0][2], down[0][1], down[0][0], left[0][2], left[0][1], left[0][0],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[0][2], left[0][1], left[0][0], up[2][0], up[2][1], up[2][2], right[0][2], right[0][1], right[0][0], down[0][2], down[0][1], down[0][0], = \
                    up[2][0], up[2][1], up[2][2], right[0][2], right[0][1], right[0][0], down[0][2], down[0][1], down[0][0], left[0][2], left[0][1], left[0][0],
            cube[0][0][1] = nex
        elif cmd[0] == 'D':
            cur = cube[0][0][-1]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][-1][0]  # 2행
            right = cube[1][0][0]  # 2행
            down = cube[0][1][0]  # 0행
            left = cube[-1][0][0]  # 2행
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[2][0], right[2][1], right[2][2], down[0][2], down[0][1], down[0][0], left[2][0], left[2][1], left[2][2], up[2][0], up[2][1], up[2][2], =\
                    up[2][0], up[2][1], up[2][2], right[2][0], right[2][1], right[2][2], down[0][2], down[0][1], down[0][0], left[2][0], left[2][1], left[2][2],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[2][0], left[2][1], left[2][2], up[2][0], up[2][1], up[2][2], right[2][0], right[2][1], right[2][2], down[0][2], down[0][1], down[0][0], = up[2][0], up[2][1], up[2][2], right[2][0], right[2][1], right[2][2], down[0][2], down[0][1], down[0][0], left[2][0], left[2][1], left[2][2],
            cube[0][0][-1] = nex
        elif cmd[0] == 'F':
            cur = cube[0][-1][0]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][0][1]  # 2행
            right = cube[1][0][0]  # 0열
            down = cube[0][0][-1]  # 0행
            left = cube[-1][0][0]  # 2열
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[0][0], right[1][0], right[2][0], down[0][2], down[0][1], down[0][0], left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], =\
                    up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], down[0][2], down[0][1], down[0][0], left[2][2], left[1][2], left[0][2],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], down[0][2], down[0][1], down[0][0], = \
                    up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], down[0][2], down[0][1], down[0][0], left[2][2], left[1][2], left[0][2],
            cube[0][-1][0] = nex
        elif cmd[0] == 'B':
            cur = cube[0][1][0]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][0][-1]  # 2행
            right = cube[1][0][0]  # 2열
            down = cube[0][0][1]  # 0행
            left = cube[-1][0][0]  # 0열
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[2][2], right[1][2], right[0][2], down[0][2], down[0][1], down[0][0], left[0][0], left[1][0], left[2][0], up[2][0], up[2][1], up[2][2], = \
                    up[2][0], up[2][1], up[2][2], right[2][2], right[1][2], right[0][2], down[0][2], down[0][1], down[0][0], left[0][0], left[1][0], left[2][0],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[0][0], left[1][0], left[2][0], up[2][0], up[2][1], up[2][2], right[2][2], right[1][2], right[0][2], down[0][2], down[0][1], down[0][0], = \
                    up[2][0], up[2][1], up[2][2], right[2][2], right[1][2], right[0][2], down[0][2], down[0][1], down[0][0], left[0][0], left[1][0], left[2][0],
            cube[0][1][0] = nex
        elif cmd[0] == 'L':
            cur = cube[-1][0][0]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][0][1]  # 0열
            right = cube[0][-1][0]  # 0열
            down = cube[0][0][-1]  # 0열
            left = cube[0][1][0]  # 0열
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[0][0], right[1][0], right[2][0], down[0][0], down[1][0], down[2][0], left[0][0], left[1][0], left[2][0], up[0][0], up[1][0], up[2][0], = \
                    up[0][0], up[1][0], up[2][0], right[0][0], right[1][0], right[2][0], down[0][0], down[1][0], down[2][0], left[0][0], left[1][0], left[2][0],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[0][0], left[1][0], left[2][0], up[0][0], up[1][0], up[2][0], right[0][0], right[1][0], right[2][0], down[0][0], down[1][0], down[2][0], = \
                    up[0][0], up[1][0], up[2][0], right[0][0], right[1][0], right[2][0], down[0][0], down[1][0], down[2][0], left[0][0], left[1][0], left[2][0],
            cube[-1][0][0] = nex
        elif cmd[0] == 'R':
            cur = cube[1][0][0]
            nex = [[''] * 3 for _ in range(3)]
            nex[1][1] = cur[1][1]
            up = cube[0][0][1]  # 2열
            right = cube[0][1][0]  # 2열
            down = cube[0][0][-1]  # 2열
            left = cube[0][-1][0]  # 2열
            if cmd[1] == '+':
                nex[0][2], nex[1][2], nex[2][2], nex[2][1], nex[2][0], nex[1][0], nex[0][0], nex[0][1] = cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                right[2][2], right[1][2], right[0][2], down[2][2], down[1][2], down[0][2], left[2][2], left[1][2], left[0][2], up[2][2], up[1][2], up[0][2], = \
                    up[2][2], up[1][2], up[0][2], right[2][2], right[1][2], right[0][2], down[2][2], down[1][2], down[0][2], left[2][2], left[1][2], left[0][2],
            elif cmd[1] == '-':
                nex[2][0], nex[1][0], nex[0][0], nex[0][1], nex[0][2], nex[1][2], nex[2][2], nex[2][1]= cur[0][0], cur[0][1], cur[0][2], cur[1][2], cur[2][2], cur[2][1], cur[2][0], cur[1][0]
                left[2][2], left[1][2], left[0][2], up[2][2], up[1][2], up[0][2], right[2][2], right[1][2], right[0][2], down[2][2], down[1][2], down[0][2], = \
                    up[2][2], up[1][2], up[0][2], right[2][2], right[1][2], right[0][2], down[2][2], down[1][2], down[0][2], left[2][2], left[1][2], left[0][2],
            cube[1][0][0] = nex
    up = cube[0][0][1]
    for i in range(3):
        for j in range(3):
            print(up[i][j], end='')
        print()