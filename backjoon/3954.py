import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    m, c, i = map(int, input().rstrip().split(' '))
    prog = input().rstrip()
    line = input().rstrip()