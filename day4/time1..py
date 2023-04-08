# time 모듈
import time

# 1070.01.01 이후의 지금까지의 시간을 초로 계산 #컴퓨터가 70년도에 나와서 그냥 70년으로 해봄
print(time.time()) #time함수가 70년 1월1일부터 계산해준다

#년과 일로 환산
year = round(time.time()/(365*24*60*60))
print(year)
day = round(time.time()/(24*60*60))
print(day)

# 수행시간 출력하기
#1부터 10까지 출력하기
start = time.time() #시작 시간
for i in range(1, 11):
    print(i)
    #time.sleep(1) #time.sleep함수 는 1초에 한번씩 출력해준다
    time.sleep(0.5) #0.5초에 한번씩 출력

end = time.time() #끝나는 시긴
print(f'수행시간 : {end-start:0.3f}초') #이걸 수행하는데 얼마나 걸렸는지 계산
#0.3f는 소수 3째 자리 까지 출력