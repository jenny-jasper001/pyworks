점수 = 55 #내 점수 75때
if 점수 >= 60:  #60점 이상시 합격
    print("합격") # 합격시
else:  #불합격시
    print("불합격")

i = 0 #반복 변수 = 0 #반복변수 0임
while i < 10:  #(1부터 10까지 출력)
    i+=1   #i =1+1    
    print(i, end='')

i = 0
while True: #true여야 실행
    i+= 1
    if i> 10:
       break;
    print(i, end='')
