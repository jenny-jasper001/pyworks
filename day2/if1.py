"""
#제한 속도가 50km이상이면"속도위반"
# 아니면 "속도준수"
# if 조건

limit_speed = 55  #limit_speed 에 55을 담다 지금 내가 55km로 달리고 있다
if limit_speed >= 50: #55가 50보다 크거나 같다 -> true
    print("속도 위반") # 들여쓰기, 인덴트


#이건 조건문 중 if 단독문이다

#조건문(if ~ else 문)
#제한 속도가 50km이상이면 "속도위반, 과태료 10만원"이고
#50km 미만이면 "안전 속도 준수"

limit_speed = 49
if limit_speed >= 50:
    print("속도위반, 과태료 10만원")
else: #limit_speed <50라는 의미가 숨어있다
    print("안전 속도 준수")


# 시험점수가 60점 이상이면 "합격", 아니면 "불햡격" 판정하기
#시험점수 라는 걸 변수에 담아야 한다
점수 = 55
if 점수 >= 60:
    print("합격")
else:
    print("불합격")

"""

#어떤수를 입력받아서 짝술와 홀수로 출력하세요
num = int(input("숫자 입력: ")) # 입력은 문자가 입력된다 오류가나옴 int함수를 붙여줘야됨
if num % 2 == 0:  # 나누기 2에서 0이 나오면 짝수 1인 나오면 홀수
    # %는 나머지 연산자 이다
    print("짝수")
else:
    print("홀수")


