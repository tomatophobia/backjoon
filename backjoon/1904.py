# a: 00 타일의 갯수
# b: 1 타일의 갯수
# 지금까지 뽑은 타일 조합
def f(a, b, res):
    if a == 0 and b == 0:
        return res
    if a == 0:
        # 무조건 1
        next = res[:]
        if len(res) == 0:
            next.append("1")
        else:
            next[0] += "1"
        return f(a, b - 1, next)
    elif b == 0:
        # 무조건 00
        next = res[:]
        if len(res) == 0:
            next.append("00")
        else:
            next[0] += "00"
        return f(a - 1, b, next)
    else:
        # 두 가지 모두
        next = res[:]
        if len(res) == 0:
            next.append("1")
        else:
            next[0] += "1"
        x = f(a, b - 1, next)
        next = res[:]
        if len(res) == 0:
            next.append("00")
        else:
            next[0] += "00"
        y = f(a - 1, b, next)
        return x + y


n = int(input())
s = set()

# i는 0의 갯수, j는 1의 갯수
for i in range(n // 2 + 1):
    j = n - 2 * i
    c = f(i, j, [])
    print(c)
    for elem in c:
        s.add(elem)
print(len(s))
