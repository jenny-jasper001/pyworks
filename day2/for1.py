# for문을 이용한 반복문
# 1부터 10까지 출력, 합계

i = 0
while i < 10:
    i = i + 1
    print(i, end='') #end붙이면12345678910로 아래로 출력되다가 옆으로 출력된다
print()
print('=' *30)  # *곱하기는 옆으로 생긴다
#한칸 떼고 =가 30개 생긴다

#range(시작값, 종료값, 증감값이다)  증감값이 1인 경우는 생략이 가능
#range(0,11) = range(0,11,1)
for i in range(0, 11, 1): #11에서 1을 뺀것 (0,11)은 0부터 10까지 줄력된다 하나의 약속
    print(i)

#1부터 10까지 홀수 출력
for i in range(1, 11, 2):  
    print(i)

#1부터 10까지 짝수 출력
for i in range(1, 11,):
    if i % 2 == 0:
        print(i)

#1부터 10까지의 합계
sum_v = 0
for i in range(11): #range( 0, 11 ,1) = range(11)
    #sum_v = sum_v + i
    sum_v += i

print("합계:", sum_v)
