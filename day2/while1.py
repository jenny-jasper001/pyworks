"""
#반복문 while 조건문은 if

i = 1 #메모리 i라는 변수에 0을 할당, 처음 시작할때 시작값이 있어야 한다
while i < 11: #종료값(비교조건)
    print("안녕", i)
    i = i +1 #증가값
    

#숫자 0~1까지 출력
n = 0
while n < 10:
    #n = n + 1
    print(n)

#n= 0 true n=1, 1
#n= 1 true n=2 , 2
#n= 2 true n=3, 3
#n= 3 true n=4 , 4
#n= 4 true n=5, 5
#n= 5 true n=6, 6
#n= 6 true n=7 , 7
#n= 7 true n=8, 8
#n= 8 true n=9, 9
#n= 9 true n=10, 10
#n= 10 false   루프 밖으로 빠져나감


# 1부터 10까지의 합계
sum_v = 0  #sum같이 보라색으로 나오는 함수는 이름으로 쓸때 다른거 같이스삼
sum_v = sum_v + 1
sum_v = sum_v + 2
sum_v = sum_v + 3
sum_v = sum_v + 4
print(sum_v)
"""
i = 0
sum_v = 0

while i < 10:
    i = i + 1
    sum_v = sum_v + i
    print("i=", i , "sum_v", sum_v)
    
print("합계:", sum_v)
