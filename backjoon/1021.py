import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

cnt = 0

l = list(map(int, input().split(' ')))
while len(l) > 0:
    i = l[0]
    if i - 1 <= n - i + 1:
        cnt += i - 1
    else:
        cnt += n - i + 1
    n -= 1
    l.pop(0)
    # 이게 O(n)이라서 전체가 O(n^2) 이 될 것 같은데 더 좋은 방법 없나?
    for j in range(len(l)):
        l[j] = l[j] - i if l[j] - i > 0 else l[j] - i + n + 1
print(cnt)

# 일단 Greedy 접근이 맞음

# 1등 답을 보니까 list.index 함수를 씀. 시간 복잡도 측면에서 더 좋은 방법은 없는 듯
'''
1등 코드 참고
n, m = map(int, input().split())
dq = [i for i in range(1, n+1)]

ans = 0

for find in map(int, input().split()):
    ix = dq.index(find)
    ans += min(len(dq[ix:]), len(dq[:ix]))
    dq = dq[ix+1:] + dq[:ix]

print(ans)
'''
