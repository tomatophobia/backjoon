import sys

input = sys.stdin.readline

primes = []

for i in range(2, 246912):
    ispr = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            ispr = False
            break
    if ispr:
        primes.append(i)

while True:
    num = int(input())
    if num == 0:
        break

    count = 0
    for p in primes:
        if num < p <= num * 2:
            count += 1
        if p > num * 2:
            break
    print(count)
