import sys

input = sys.stdin.readline

t = int(input())

dp = [-1] * 41
dp[0] = 0
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(t):
    x = int(input())
    if x == 0:
        print("1 0")
    else:
        print(dp[x-1], dp[x])
