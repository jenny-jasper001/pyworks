#함수의 정의와 호출

# print("안녕") 만들어서 필요할때 호출
#입력기능 - input(), 함수가 입력기능을 가진다
#def 함수이름():
def hello(): #def 정의 hello라는 함수 만들
    print("hello~ Python!")
    
#"hello~ Python!"말고 다른거 부르고 싶을때
def hello2(name):  #매개변수
    print("hello", name)
    
#호출(call) - 사용
hello()
hello2("홍길동")
hello2("jerry")
