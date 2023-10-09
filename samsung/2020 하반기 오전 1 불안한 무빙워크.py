import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

N, K = map(int, input().rstrip().split(' '))
walk = deque(list(map(int, input().rstrip().split(' '))))
people = deque([False] * N)

count = 0
while True:
    count += 1
    # 무빙워크 1칸 이동
    walk.appendleft(walk.pop())
    people.pop()
    people.appendleft(False)
    if people[N - 1]:
        people[N - 1] = False
    # 사람 이동
    for pi in range(N - 2, -1, -1):
        if not people[pi]:
            continue
        if walk[pi + 1] > 0 and not people[pi + 1]:
            people[pi] = False
            people[pi + 1] = True
            walk[pi + 1] -= 1
            if pi + 1 == N - 1:
                people[pi + 1] = False
    # 1번 칸 올리기
    if not people[0] and walk[0] > 0:
        people[0] = True
        walk[0] -= 1
    # 종료 조건
    broke = 0
    for ww in walk:
        if ww == 0:
            broke += 1
    if broke >= K:
        break
print(count)
