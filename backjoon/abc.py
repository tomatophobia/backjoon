x = 1  # assign
y = 2

# 숫자 (정수) int
x = 1
x = 3
x = -6

# 숫자 (유리수) float
x = 1.1
x = 3.2
x = -3.5

# 연산자
x = 1 + 2
x = 1 - 2
x = 1 * 2
x = 1 / 2
x = 1 // 2
x = 1 % 2
x = 1 == 2
x = 1 != 2

# 부등호
x = 1 < 2
x = 1 <= 2
x = 1 > 2
x = 1 >= 2
x = 1 == 2
x = 1 != 2

# 참, 거짓 boolean (bool)
x = True
x = False

# 논리 연산자
x = True and False
x = True or False
x = not False

# 문자열 string (str)
x = 'abc'

# 리스트 list
x = [1, 2, 3]


## 조건문
# if
x = 3
# x가 홀수일 때는 "홀수!", 짝수일 때는 "짝수!" 라고 print해라
if x % 2 == 1:
    print('홀수!')
else:
    print('짝수!')

# x가 3보다 크면 "!!!", 0보다 크고 3보다 작거나 같으면 "!!", 0보다 작거나 같으면 "!" 를 프린트해라
if x > 3:
    print('!!!')
elif 0 < x and x <= 3:  # else if
    print('!!')
else:
    print('!')


## 반복문
# for

# while
# 1부터 100까지 프린트하는 프로그램
x = 1
while x <= 100:
    print(x)
    x = x + 1
