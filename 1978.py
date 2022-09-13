import math

N = int(input())

l = map(int, input().split(' '))

count = 0
for i in l:
    if i == 1:
        continue

    mid = int(math.sqrt(i))

    isPrime = True
    for x in range(2, mid + 1):
        if i % x == 0:
            isPrime = False
            break

    if isPrime:
        count += 1
print(count)
