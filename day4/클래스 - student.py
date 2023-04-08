# 학생 클래스(student)
#클래스 이름은 첫글자가 대문자이다

class Student:

    # __int__가 클래스에 꼭 들어간다
    def __init__(self): #초기자(함수)
         self.name = "이순신"
         self.grade = 1

#클래스에서 객체로 만들어주면 메모리가 된다
s1 = Student()
#print(s1. ) #객체(인스턴스) 생성(객체 변수 - 메모리에서 실행됨)
#s1이 붕어빵이다 s1이 메모리에서 실행된다 .을 찍어주면 s1의 모든것이 들어간다는 소리
print(f'이름 :{s1.name}')
print(f'학년 :{s1.grade}')