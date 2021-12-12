import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split(' '))

box = []
queue = deque()
for i in range(n):
    line = []
    spl = input().split(' ')
    for j in range(len(spl)):
        jj = int(spl[j])
        line.append(jj)
        if jj == 1:
            queue.append((i, j))
    box.append(line)

drt = [(1, 0), (0, 1), (0, -1), (-1, 0)]
count = 0
while len(queue) > 0:
    oneq = deque()
    for i in range(len(queue)):
        oneq.append(queue.popleft())

    changed = False
    while len(oneq) > 0:
        x, y = oneq.popleft()
        for dx, dy in drt:
            x_dx = x + dx
            y_dy = y + dy
            if 0 <= x_dx < n and 0 <= y_dy < m and box[x_dx][y_dy] == 0:
                changed = True
                box[x_dx][y_dy] = 1
                queue.append((x_dx, y_dy))
    if changed:
        count += 1

zero = False
for l in box:
    for b in l:
        if b == 0:
            print(-1)
            exit(0)
print(count)