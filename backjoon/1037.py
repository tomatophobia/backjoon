import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split(' ')))
l.sort()
# sorting 안하고 최대, 최솟값 구하면 O(N) 타입에 끝낼 수 있음. 근데 통과했으니까.. ㅎ
print(l[0] * l[-1])
