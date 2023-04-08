#random 모듈
import random
#random안의 randint가 있다
#randint(시작값, 끝수) - 시작수와 끝수 사이의 정수 중에서 난수값 발생
#choice(리스트) - 리스트 안에서 무작위로 선정
#1부터 10까지 자연수 중 랜덤하게 1개 출력
num = random.randint(1, 10) #숫자를 1부터 10까지 랜덤적으로 출력시킴
print(num)

#주사위를 1개 만들기
#dice = random.randint(1, 6)
#print(dice)

#주사위 10번 던지기
for i in range(10):
    dice = random.randint(1,6)
    print(dice)

fruit = ['apple', 'strawberry', 'banana']
f = random.choice(fruit)
print(f)
#리스트 choice, 숫자는 randint로 상용 (random사용시)

#리스트 항목을 무작위로 섞기
random.shuffle(fruit)
print(fruit)


