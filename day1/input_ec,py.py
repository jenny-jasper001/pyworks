"""
#입력함수 -> input()

print("문자 입력: ")
text = input()
print(text)

# 단축표현
text = input("문자 입력: ")
print(text)

#숫자 입력
num = input("숫자 입력 : ") #num은 문자이다
num = int(num) #int()함수로 숫자로 변환한다
print(num - 10)
#shell에 숫자입력 후 숫자입력: 한후 숫자(예12 입력시 12가 출력되는데 숫자가 아니라 문자가 출력되는거다


#단축표현법
num = int(input("숫자 입력:" ))
print(num-10)

#문자열 빼기
print(num)
print(num-10)
num = int(num) #int()함수로 숫자로 변환한다
print(num - 10)


#문자열 더하기
print("대한" + "민국")

#문자열 곱하기
print("지구"*3)
print("="*3)
#이런 경우 shell에 지구지구지구, ===이 이렇게 3번식 나온다
"""

#이름은 ~입니다 이름은 홍길동입니다
#나이는 ~세입니다 나이는 몇살입니다
name = input("이름 입력: ")
#print("이름은", name , "입니다")  이름은 ghdrlfehd 입니다 로 출력된다
print("이름은 "+ name + "입니다")

age = int(input("나이 입력:" ))
#print("나이는", age , "입니다")
print("나이는 "+ str(age) + "세입니다") #age는 숫자니까 문자로 고쳐주는 str()함수로 해줍니
