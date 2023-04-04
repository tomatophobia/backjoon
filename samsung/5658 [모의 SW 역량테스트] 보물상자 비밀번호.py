import sys
from queue import PriorityQueue

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input().rstrip())
for test_case in range(1, T + 1):
    N, K = map(int, input().rstrip().split(' '))
    k = N // 4
    ns = input().rstrip()
    nums = set()
    for i in range(0, 4):
        for j in range(0, k):
            if i < 3:
                nums.add(ns[i * k + j:(i + 1) * k + j])
            else:
                nums.add(ns[i * k + j:(i + 1) * k + j] + ns[:j])
    result = int(sorted(nums)[-K], 16)

    print(f"#{test_case} {result}")
