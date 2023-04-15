#비행기 클래스
class Airplane:
    def __init__(self, brand):
        self.brand = brand
    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")

#메인 영역
#if문을 써줘야 이게 메인영역이라고 알릴수 있다, if문이 없으면 use_module파일에 밑에 내용이 출력이 된다
if __name__ == "__main__":    #if는 조건문이라 ==같다 표시해줌
    air1 = Airplane("대한항공")
    print("항공사 :", air1.brand)
    air1.take_off()
    air1.fly()
    air1.land()



