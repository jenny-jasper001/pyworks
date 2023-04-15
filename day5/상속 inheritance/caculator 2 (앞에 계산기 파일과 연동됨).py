#Calculator 계산기.py를 상속받음
#Calculator 계산기는 더하기 빼기만 했는데 이건 제곱, 나누기 가능
from calculator import Calculator   #Calculator - 클래스 이름 #calculator 파일 이름(공백 있으면 안됨) 앞에 calculator.py파일 말하는 거임

class MoreCalculator(Calculator):
    def pow(self):  #pow 거듭제곱의 연산자
        return self.x ** self.y

mcal = MoreCalculator(2, 3)
print(mcal.pow()) #2x2x2 = 8 이 출력