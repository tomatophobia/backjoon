import sys

input = sys.stdin.readline

x = int(input())

num = 0
while True:
    snum = str(num)
    three = 0
    for s in snum:
        if s == '6':
            three += 1
        else:
            three = 0
        if three == 3:
            break
    if three == 3:
        x -= 1
        if x == 0:
            break
    num += 1
print(num)