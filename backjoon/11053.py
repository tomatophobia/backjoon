import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split(' ')))

dp = [0] * n
dp[1] = 1

for i in range(1, n):
    for j in range(i):
        if l[j] < l[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))

'''
d[i] -> l[i] 가 포함된 LIS
d[n] = max(1<=i<n, l[i] < l[n])(d[i]) + 1  (max값이 없는 경우 0)
그리고 max(d)

개같은 점
1. 새롭게 구한 풀이에서 max(dp)를 해야 하는 이유를 떠올리지 못했음
dp를 잘못 이해함. 길이 i 까지 LIS가 아니고 l[i]가 포함된 LIS 여서 max를 때려줘야 함.

2. dp[i] += 1 을 바깥으로 안 빼면 문제되는 이유를 찾지 못했음
찾음 l[i]가 전체 중에 최솟값이면 자기 자신 하나라서 1이어야 하는데 처음 default 값을 0으로 설정해놓아서 +1은 최소 한 번 해주어야 했음.
코드는 수정했음.

3. 기존 풀이에서 안되는 이유를 못찾음
아래는 기존 풀이
import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split(' ')))
k = 0
for i in l:
    if k < i:
        k = i

dp = [[None] * (k + 1) for _ in range(n + 1)]
dp[0] = [0] * (k + 1)

l0 = l + [0]
for i in range(1, n + 1):
    for j in l0:
        if l[-i] < j: -> 여기가 틀렸음 j랑 같아도 포함될 수 있으므로 l[-i] <= j 임
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(1 + dp[i - 1][l[-i]], dp[i - 1][j])

print(dp[n][0])
'''
