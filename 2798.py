import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

c = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                s = cards[i] + cards[j] + cards[k]
                if c < s <= m:
                    c = s

print(c)
