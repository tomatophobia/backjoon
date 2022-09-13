import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    ps = input().rstrip()
    st = []
    flag = False
    for p in ps:
        if p == '(':
            st.append(p)
        elif p == ')':
            if len(st) != 0 and st[-1] == "(":
                st.pop()
            else:
                print("NO")
                flag = True
                break
    if flag:
        continue
    if len(st) == 0:
        print("YES")
    else:
        print("NO")

# YES라고 프린트해야 하는데 Yes라고 했음 조심하자
