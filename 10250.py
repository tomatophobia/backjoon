import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split(' '))
    x = (n - 1) // h + 1
    y = (n - 1) % h + 1
    print(f'{y}{x:02d}')