import sys

input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

# Dynamic Programming Table
d = [0 for i in range(n)]

for i in range(1, n):
    if i < 3:
        d[i] = l[-1]
    else:
        d[i] = max(l[-i] + l[-i + 2] + d[i - 3], l[-i + 1] + d[i - 2])


a = l[0] + d[n-1] if n >= 1 else -1
b = l[1] + d[n-2] if n >= 2 else -1
c = l[0] + l[1] + l[3] + d[n-4] if n >= 4 else -1

print(max(a, b, c))

'''
엄청 실수를 많이 함. 처음에 풀이는 금방 떠올렸는데...
1. 재귀함수 사용 -> 탑다운으로 다이나믹 프로그래밍을 메모이제이션 없이 구현하면 존1나 느려짐
2. 연속한 계단 3개 조건 -> 처음 땅바닥은 계단이 아니면서 연속한 3개의 계단이라는 조건을 이해하는데 오래걸림
3. 자잘한 코딩 실수 -> 2번까지 알았음에도 자잘한 실수들이 계속 나와서 문제를 못 맞춤. 반복문을 너무 안썼던 듯
'''
