import sys
import functools

input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split(' '))))


def compare(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        else:
            return 0


l.sort(key=functools.cmp_to_key(compare))
for i in l:
    print(i[0], i[1])

'''
import sys

lst = sys.stdin.readlines()[1:]
lst.sort(key=lambda x: int(x.split()[0]))
lst.sort(key=lambda x: int(x.split()[1]))
print(''.join(lst))

인상적인 풀이
'''
