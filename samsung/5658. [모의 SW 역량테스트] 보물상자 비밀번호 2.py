import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().rstrip().split(' '))
    nums = list(input().rstrip())
    n4 = N // 4
    s = set()
    for i in range(n4):
        for j in range(3):
            s.add(''.join(nums[i + n4 * j: i + n4 * j + n4]))
        s.add(''.join(nums[i + n4 * 3:] + nums[:i]))
    li = list(s)
    li.sort(reverse=True)
    print(f'#{test_case} {int(li[K-1], 16)}')
