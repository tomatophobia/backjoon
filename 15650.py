import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split(' '))
l = [i for i in range(1, n+1)]

for c in combinations(l, m):
    print(' '.join(map(str, c)))

'''
itertools 안 썼다면 재귀함수로
재귀함수도 안 썼다면 while문과 stack으로 구현하면 될 듯?
'''
