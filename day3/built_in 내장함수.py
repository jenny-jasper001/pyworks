#내장 함수
#절대값
print(abs(-4)) #abs 절대값 함수
print(abs(4))

#round 반올림 함수
#round(number, 자리수)
print(round(2.56)) #정수로 반올림 #round(2.56) = round(2.56, 0)
print(round(2.56, 1)) #소수 첫째자리로 반올림
print(round(1256, -1))

# 최대값 - max()
max_v = (max([3, 1, 8]))
min_v = (min([3, 1, 8]))
print(max_v) #max 는 8이다
print(f'최대값 : {max_v}')
print(f'최소값 : {min_v}')      

# 소수점 버림 - floor()
#floor() floor만 치면 안나옴 math.하고 기다리면 함수들이 든다
#수학 관련 모듈
import math
print(math.floor(2.56))
