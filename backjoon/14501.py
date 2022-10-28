import sys

input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]
for i in range(N):
    t, p = map(int, input().rstrip().split(' '))
    T.append(t)
    P.append(p)

# D(i, j) = Max_i( P(i) + D(i + T(i), j) )
# j가 딱히 안쓰이므로 D(i, j) = D(i)
D = [0] * (N + 1)  # D(N) ~> D(1) 까지 순서대로

for i in range(N, 0, -1):
    max_v = 0
    for j in range(i, N + 1):
        v = 0
        if j + T[j] == N + 1:
            v = P[j]
        elif j + T[j] <= N:
            v = P[j] + D[j + T[j]]
        if v > max_v:
            max_v = v
    D[i] = max_v
print(D[1])
