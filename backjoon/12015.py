import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split(' ')))

active = []

for e in l:
    if len(active) == 0 or active[-1] < e:
        active.append(e)
    else:
        start = 0
        end = len(active) - 1
        mid = (start + end) // 2
        while start < end:
            if active[mid] >= e:
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2
        active[mid] = e
print(len(active))

'''
PyPy3로만 통과함.. ㅅㅂ
Python3로 통과한 사람들 보니까 bisect라는 라이브러리 써서 바이너리 서치를 하는 것 같고 그거 안쓴 사람은 처음 리스트 입력받을 때 map 결과를 바로 리스트로 변환 안하고 iterator처럼 씀
https://eine.tistory.com/entry/가장-긴-증가하는-부분-수열LIS-Longest-Increasing-Subsequence
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

1. active list에 길이가 각기 다른 LIS 후보가 될 수 있는 리스트들을 관리한다.
길이가 같은 리스트가 여러 개 있을 필요가 없다. 만약 두 리스트의 길이가 같다면 마지막 원소가 더 작은 것이 모든 경우에 더 유리하므로 마지막 원소가 작은 하나만 있으면 된다.
2. “end element of smaller list is smaller than end elements of larger lists“
해당 성질에 의해서 길이가 다른 각기 다른 리스트들을 n*n 공간에 저장할 필요 없이 하나의 리스트로 겹쳐서 관리할 수 있다.
'''
