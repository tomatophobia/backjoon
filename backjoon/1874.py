import sys

input = sys.stdin.readline

s = int(input())

num = [i for i in range(s, 0, -1)]
st = []
result = ''

m = 0
for i in range(s):
    x = int(input())
    if x > m:
        result += '+\n' * (x - m) + '-\n'
        for j in range(x - m):
            st.append(num.pop())
        st.pop()
        m = x
    else:
        p = st.pop()
        if x != p:
            result = 'NO'
            break
        result += '-\n'

print(result.rstrip())

'''
엄청 오래걸림. 시간 초과로 많이 틀렸는데 틀린 이유 정리
1. x in list -> 파이썬에서 리스트가 원소를 가지고 있는지 확인하는게 O(N)이 걸릴 것 같아서 제거
2. list += 사용 -> 반복문 돌면서 하나씩 집어넣는 것보다 느린가봄. 스칼라는 +=이 느린 줄 알고 있었는데 파이썬도 그런가?
3. list 슬라이싱 사용 -> list에서 pop 여러번 하는 대신 슬라이싱으로 잘랐는데 느린가?

1번은 O(N)이 맞고, 2번은 O(A + B)여서 2번도 문제였음.
3번은 찾아보니까 슬라이싱 자체는 pop 여러번 하는 거랑 똑같은데 내가 슬라이싱을 전체를 양분하기 위해서 2번 써서 결국 O(N)처럼 쓰고 있었던게 얽혀서 문제가 된 듯

1등 답을 보니까 string 안쓰고 result 리스트에 +, - 추가하던데 그게 더 빠를 수도 있을 듯
또한 나처럼 max를 관리하지 않고 지금까지 num에서 몇 개 뺐는지 current를 써서 함. 이렇게 하면 num 리스트도 없애니까 더 빨리질 듯 
'''
