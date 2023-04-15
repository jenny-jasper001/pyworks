# dog 클래스 생성
class Dog:
    def __init__(self, name, type): #type 강아지 종류
        self.name = name
        self.type = type

    def bark(self): #bark 강아지의 행동
        print(f"{self.type}이 짖어요.!")

#메인영역인걸 알려줘야 한다
if __name__ == "__main__":
    dog1 = Dog('사랑이', '푸들')
    print("강아지 이름:", dog1.name)
    print("강아지 종류:", dog1.type)
    dog1.bark()

    dog2 = Dog('돌쇠', '진돗개')
    print("강아지 이름:", dog2.name)
    print("강아지 종류:", dog2.type)
    dog2.bark()
    dog2 = Dog('돌쇠', '진돗개')

