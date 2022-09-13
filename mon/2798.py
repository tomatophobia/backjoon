n, m = map(int, input().split(' '))
l = list(map(int, input().split(' ')))

maxsum = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = l[i] + l[j] + l[k]
            if (sum <= m):
                if (maxsum < sum):
                    maxsum = sum

print(maxsum)
