# 계산기 #클래스 - 상속
class Calculator:
    def __init__(self, x, y): #def 정의
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self): #빼기 함수 sub
        return self.x - self.y

if __name__ == "__main__": # "": 뒤의 밑에는 꼭 들여쓰기 해주기
    cal = Calculator(10, 20)
    #print(cal.x, cal.y)
    print(cal.add())    #30이 출력된다 #더하기 함수 add
    print(cal.sub())    #-10이 출력

