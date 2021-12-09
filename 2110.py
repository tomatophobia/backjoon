import math
import sys
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split(' '))

l = []
for i in range(n):
    l.append(int(input()))
l.sort()

maxl = max(l)
minl = min(l)

k = maxl - minl

start = 1
end = math.floor(k / (c - 1))

while start < end:
    mid = (start + end + 1) // 2  # 최댓값 구하기, 최솟값 구하기인 경우 (start + end) // 2

    before = -1
    count = c  # 배치해야 하는 공유기 갯수 가장 왼쪽에 하나 꽂기
    for i in l:
        if before == -1:
            count -= 1
            before = i
        else:
            if i - before >= mid:
                count -= 1
                before = i
        if count == 0:
            break
    condition = count == 0
    # TODO condition 함수 엄밀성 부족

    if condition:
        start = mid
    else:
        end = mid - 1

mid = (start + end + 1) // 2  # 마지막에 condition false로 끝났을 때 한 칸 이동
print(mid)

'''
https://ialy1595.github.io/post/parametric-search/ 본호야 고맙다

문제 생각의 경로
우선 가능한 최댓값의 범위가 [1, floor(max - min) / c - 1)] 이라는 것을 유추했음
그 다음 존1나 고민하다가 이 문제가 parametric search로 푼다는 것을 알게 됨. 본호 블로그 정독
범위는 이미 알았으니까 여기서 이진탐색을 하는데 condition 함수가 고민됨
생각해보니까 x 간격으로 공유기 꽂기가 가능한가로 condition 가능해보여졌음. 근데 위의 코드는 엄밀성이 부족. 안될 때 다른 방법이 없다는 증명이 없어서...
제출하니까 잘 돌아감 ㅋ
'''
