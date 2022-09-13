import sys

input = sys.stdin.readline


def fun(num, fr, to):
    if num == 1:
        print(fr, to)
    else:
        next_to = [1, 2, 3]
        next_to.remove(fr)
        next_to.remove(to)
        next_to = next_to[0]
        fun(num-1, fr, next_to)
        print(fr, to)
        fun(num-1, next_to, to)


n = int(input())

print(2**n - 1)
fun(n, 1, 3)
