import sys

input = sys.stdin.readline

k = int(input())

st = []
for i in range(k):
    x = int(input())
    if x == 0:
        st.pop()
    else:
        st.append(x)
print(sum(st))
