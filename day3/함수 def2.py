#return이 있는 함수
#매개 변수가 1개인 함수
#제곱수를 계산하는 함수
def square(x): #square는 제곱수를 의미
    return x * x

#print(square(2)) #우리가 함수를 만든것
#print(square(5)) 하면 25나옴, print(square(6))하면 36나옴
#1이 증가하는 함수
def one_up(x): #매개변수 x한개
    x = x + 1
    return x 

print(one_up(25))


# 매개변수가 2개 있는 함수
#두 수의 차이를 구하는 함수 - 뺄셈 함수
def sub(x, y):
    minus = x - y
    return minus

#두 수의 합을 구하는 함수 (add()함수 정의)
def add(x,y):
    plus = x + y
    return plus

#호출
val = sub(4, 7)
val2 = add(4, 7)
print("두 수의 차 = {0}".format(val)) #-3
print("두 수의 합 = {0}".format(val2)) #11

#호출
val = sub(4, 7) #먼저 호출하면서 sub를 찾고 x에 4를 y에 7을 담는다 그거 마이너스 된게 변수 minus에 담기고 다시 변수 val에 담겨 출력된다
print("두 수의 차 = {0}".format(val)) 

