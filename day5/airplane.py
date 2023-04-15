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

air1 = Airplane("대한항공")
print("항공사 :", air1.brand)
air1.take_off()
air1.fly()
air1.land()



