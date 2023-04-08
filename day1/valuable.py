#var.py 파일이름=모듈이름 나는  valuable이라고 저장함
#변수 만들기(선언)
#여러줄을 주석하는 법 """여러개의줄""" 홀따옴표를 3개씩 붙여야한다
#변수이름 만들때 주의점
#1. 숫자로 시작하면 안된다 에러가 납니다
#2.변수이름에는 공백이 들어가면 안된다 에러가 난다
#사계절 = '봄'
#print(사 계절)로 하면 에러가 난다 print(사계절)로 해야한다


"""
user = "sky2003"
print("아이디",user) 
password = "abc1234"
print("비밀번호:",password)

#사칙연산(변수를 이용해서)
num1 = 12
num2 = 5

print("더하기:", num1 + num2) #17
print("더하기:", num1 - num2) #7
print("곱하기:", num1 * num2) #60
print("나누기:", num1 / num2) #2.4
print("나누고 난 후의 나머지만 나오기:", num1 % num2) #2
print("몫:", num1 // num2) #파이선만 가지는 기호
"""

#총점과 평균
#eng는 영어점수 math는 수학점수
eng = 70 #eng변수에 70을 대입
math = 80 #math라는 변수에 80을 대입
total = eng + math #총점은 = 영어 + 수학점수
print(total)

#평균구하기, 평균 = 총점 나누기 개수
avg = total / 2 
print(avg)
#
print(type(total)) #<class 'int'>로 나온다 type가 어떤형인지 알려준다 int= 정수
print(type(avg))
#type()함수는 자료형을 알려준다, 자료형=type

#bool 자료형(논리) 다른 변수는 못들어가고 True False 만 들어갈수 있다
state = False
print(state)
print(type(state))

print(3==2) # ==r같다는 의미
# 논리 비교연산에서 3==2로 하면 틀리기 때문에 shell에 false라고 출력이 된다
print(3>2) #논리 비교 연산에서 3>2는 맞기 때문에 shell에 true라고 출력이 된다
