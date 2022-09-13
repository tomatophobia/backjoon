import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

coins = []
for i in range(n):
    coins.append(int(input()))

cnt = 0
while k > 0:
    c = coins.pop()
    cnt += k // c
    k = k % c

print(cnt)

'''
증명
맞춰야 하는 금액이 K원이라고 할 때, K보다 작거나 같은 동전 중 크기가 가장 큰 동전의 금액을 Xi라고 하자. 이때 Xi가 최적해 [X1, X2, X3, . . . , Xn]에 포함되지 않는다고 가정하자(X1 ≤ X2 ≤ . . . ≤ Xn). 그러면 X1, X2, X3, . . . , Xn은 Xi보다 반드시 작으면서 동시에 Xi의 약수이기 때문에, Xi = Xn + Xn-1 + . . . + Xn-j를 만족하는 j가 존재한다(1 ≤ j ≤ n - 1). 따라서 그것들을 Xi로 대체하면 더 좋은 최적해를 얻을 수 있으므로 가정에 모순이 발생한다. 이로써 Xi를 포함하는 최적해가 반드시 존재함이 증명된다.
그리고 이번에도 마찬가지로 전역 최적해를 얻기 위해서는 Xi 동전 하나를 제외한 나머지 동전들에 대해서도 최적해를 얻어야 한다는 점을 이용한다. 그렇지 않으면 여기서 얻는 최적해를 이용하여 더 좋은 전역 최적해를 만들 수 있기 때문이다. 따라서 같은 과정을 반복하면, 매 순간 남은 금액보다 작거나 같은 크기의 동전들 중 가장 크기가 큰 동전을 선택함으로써 전역 최적해를 얻을 수 있음이 증명된다.
출처 : https://it-eldorado.tistory.com/53

위 증명도 만족스럽지 않지만 일단 보류
참고한 fractional knapsack https://cse.hkust.edu.hk/mjg_lib/Classes/COMP3711H_Fall14/lectures/Greedy_Knapsack_Slides.pdf
'''
