#날짜 시간 관련 모듈
import datetime

# 오늘의 날짜와 시간
now = datetime.datetime.today()
print(now)
print(now.strftime("%Y, %m, %d.")) #2023-04-01 15:45:27.963120를 -> 2023, 04, 01.로 고쳐준다
print(now.strftime("%Y, %m, %d. %H:%M:%S")) #2023, 04, 01. 15:47:15

#날짜 - 년, 월, 일 출력
print("{}년".format(now.year)) #2023년
print("{}월".format(now.month)) #4월
print("{}일".format(now.day)) #1일

#시간 - 시, 분, 초
print("{}시".format(now.hour)) #15시
print("{}분".format(now.minute)) #49분
print("{}초".format(now.second)) #15초

#나이가 100세 되는 해의 연도 계산하기
today = datetime.date.today()
print(today.year)  #2023이 나온다, 모듈로 변수로 2023을 가져온것이다

age = int(input("나이 입력 : "))
result = today.year + (100 - age)
print(f'100세 되는 해는 {result}년 입니다.') #format방식이라 str로 문자로 변경해주지 않아도 된다
