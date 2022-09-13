import sys

input = sys.stdin.readline

while True:
    ps = input().rstrip()
    if ps == '.':
        break
    st = []
    flag = False
    for p in ps:
        if p == '(' or p == '[':
            st.append(p)
        elif p == ')':
            if len(st) != 0 and st[-1] == "(":
                st.pop()
            else:
                print("no")
                flag = True
                break
        elif p == ']':
            if len(st) != 0 and st[-1] == "[":
                st.pop()
            else:
                print("no")
                flag = True
                break
    if flag:
        continue
    if len(st) == 0:
        print("yes")
    else:
        print("no")
