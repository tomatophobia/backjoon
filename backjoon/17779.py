import sys

input = sys.stdin.readline

N = int(input().rstrip())

A = []
for _ in range(N):
    line = list(map(int, input().rstrip().split(' ')))
    A.append(line)

min_diff = float('inf')

for x in range(N):
    for y in range(N):
        max_people = 0
        min_people = float('inf')
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 < N and y - d1 >= 0 and y + d2 < N:
                    p = [0, 0, 0, 0, 0]
                    for r in range(N):
                        for c in range(N):
                            if 0 <= r < x + d1 and 0 <= c <= y and r + c < x + y:
                                p[0] += A[r][c]
                            elif 0 <= r <= x + d2 and y < c < N and r - c < x - y:
                                p[1] += A[r][c]
                            elif x + d1 <= r < N and 0 <= c < y - d1 + d2 and r - c > x - y + 2 * d1:
                                p[2] += A[r][c]
                            elif x + d2 < r < N and y - d1 + d2 <= c < N and r + c > x + y + 2 * d2:
                                p[3] += A[r][c]
                            else:
                                p[4] += A[r][c]
                    diff = max(p) - min(p)
                    if diff < min_diff:
                        min_diff = diff
print(min_diff)
