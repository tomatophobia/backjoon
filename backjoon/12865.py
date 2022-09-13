import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

w = [[0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    w[i][0], w[i][1] = map(int, input().split(' '))

dp = [[None] * (k + 1) for _ in range(n + 1)]
dp[0] = [0] * (k + 1)


def fun(n, k):
    global w
    global dp
    if dp[n][k] is not None:
        return dp[n][k]

    if w[n][0] > k:
        dp[n][k] = fun(n - 1, k)
        return dp[n][k]
    else:
        dp[n][k] = max(w[n][1] + fun(n - 1, k - w[n][0]), fun(n - 1, k))
        return dp[n][k]


print(fun(n, k))
