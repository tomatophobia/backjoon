import sys

input = sys.stdin.readline

s = int(input())

num = [i for i in range(s, 0, -1)]
st = []
result = []

m = 0
for i in range(s):
    x = int(input())
    if x > m:
        for j in range(x - m):
            result.append('+')
        result.append('-')
        for j in range(x - m):
            st.append(num.pop())
        st.pop()
        m = x
    else:
        p = st.pop()
        if x != p:
            result = 'NO'
            break
        result.append('-')

if result == 'NO':
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
