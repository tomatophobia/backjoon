import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split(' ')))
l.sort()

sum = 0
for q in range(len(l)):
    sum += l[q] * (n - q)

print(sum)

'''
TODO 증명 해야 함
'''
