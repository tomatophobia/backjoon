import sys

input = sys.stdin.readline

n = int(input())

k = int(input())

start = 1
end = k

mid = (start + end + 1) // 2

while start < end:
    # condition
    # mid보다 작은 숫자가 k개 미만이다 -> 이걸로 탐색 방향 결정
    lt = 0
    for i in range(1, n + 1):
        if mid > i * n:
            lt += n
        else:
            lt += (mid - 1) // i

    if lt >= k:
        end = mid - 1
    else:
        start = mid

    mid = (start + end + 1) // 2

print(mid)

'''
parametic search 적용
condition: mid 보다 작은 숫자가 k개 미만이다
condition 만족을 하는 녀석 중 최댓값 구하기

이 때 이렇게 구한 최댓값은 반드시 행렬에 포함된다.
증명)
만약 행렬에 포함되지 않는 최댓값 x가 있다고 가정
x보다 큰 수 중 처음 행렬에 포함되는 수를 y라고 하면
행렬에서 (x보다 작은 숫자 갯수) = (y 보다 작은 숫자 갯수) = (k - 1) 이다.
이 경우 x는 최댓값이 아니게 된다 -> 가정에 모순 따라서 최댓값은 항상 행렬에 포함된다. 

아쉬웠던 점
행렬에서 어떤 수 x보다 작은 숫자의 갯수를 구하는 방법을 떠올리지 못했음
'''
