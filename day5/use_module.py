# Airplane 클래스 사용
from airplane import Airplane #airplane 모듈(파일이름) , Airlane(대문자 ,클래스 첫글자는 대문자인다)
from dog import Dog #dog파일 클래스 사용

air = Airplane("제주항공")
print(f'비행사 : {air.brand}')
air.take_off() #이륙 (airplane 파일에서 한거)
air.fly() #비행
air.land() #착륙

#dog 클래스 사용해 보기
dog = Dog('해피', '불독')
dog.bark()
