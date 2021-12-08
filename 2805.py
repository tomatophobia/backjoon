import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

l = list(map(int, input().split(' ')))

start = max(l)
end = start - m
mid = start + end // 2

while True:
    sw = 0
    for h in l:
        if h > mid:
            sw += h - mid
        if sw > m:
            break
    if sw > m:
        end = mid
    elif sw < m:
        start = mid
    else:
        anw = mid
        break

    mid = (start + end) // 2
    if start - end <= 1:
        mid = end
        break

print(mid)

'''
못 통과했던 이유...
끝나는 조건을  mid == nextMid로 미드 값이 수렵할 때까지로 돌리니까 시간 초과남...
위의 코드 조건으로 바꾸니까 해결됨...

일단 위 조건이 맞는 이유
답이 무조건 정수로 나와야 하니까 차이가 1 이하이면 두 정수 사이에 답이 있어야 하니까 가우스 기호 씌워서 넘지 않는 정수 써야 한다.

내 생각에는 mid == nextMid 일 때 무한루프가 있을 것 같은디..
아니었음 아무리 생각해도 모르겠어서 PyPy로 제출했는데 통과했음... 현기증 나버림
'''
