#리스트의 주요함수
car = ['소나타', '모닝', 'BMW']
print(car)
#스포티지 넣기
car.append('스포트티지') #append함수는 요소추가를 해주는데 맨 뒤에 추가해준다
print(car)

#요소 삭제 - pop() : 맨 뒤에서 삭제
car.pop()
print(car) #스포티지 들어간게 다시 짤린다

#특정위치에 요소 추가 - insert(인덱스, 요소)
car.insert(1, 'k7') #소나타 모닝사이에 k7을 넣고 싶을때
#[0번,1번,2번] insert(1,'k7')은 1번 자리에 k7을 넣는다는 소리

# 특정 요소 삭제 - remove(요소)
car.remove('모닝')
print(car)

#리스트의 복사, 데이터 저장
a = [1, 2, 3, 4, 5] #a라는 리스트
a2 = [] #빈 리스트 생성 #a2라는 리스트
"""
전체 복사하는 법
a2 = a
print(a2)
"""

#append() 사용하여 복사
#a2.append(1) - 하나씩 넣는 법
#print(a2)

for i in a:
    a2.append(i)
print("a2 = ", a2)

#a = [1, 2, 3, 4, 5]를 2의 배수로
#append 사용안함
# [표현식 for 항목 in 리스트]
a3 = [i*2 for i in a]
print("a3 =", a3)

"""
a3 = [] #a3이라는 빈 리스트
for i in a:
    a3.append(i*2)
   print(a3) 를 한줄로 줄여쓰면
a3 = [i*2 for i in a]
print(a3)이다.
 
    """
#3의 배수이면서 짝수 저장
#append안쓸때
b1 = [3* i for i in a if i % 2 == 0] #append에 들어갈 3* i 가 for 앞에 맨앞에 나온다
print(b1)


"""
append사용하는 유형
b1 = []
for i in a:
    if i % 2 == 0: #조건문 짝수일때만 리스트b를 넣어준다
    #홀수 일때는 if i % 1 == 0:
        b1.append(3*i)
print(b1)
"""

