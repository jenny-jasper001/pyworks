# 클래스
#변수 이름 만들때 앞에 self를 붙인다
class Student: #클래스의 첫글자는 대문자
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
            print("수업을 들어요")

s1 = Student("김하나", 1) #student1하고 차이는 밖에서 입력해준거다 __init__(self)의 밖에서 해주는게 맞는거다
print(f'{s1.name} 학생은 {s1.grade}학년입니다.')
s1.learn() #def learn(self):으로 print되어 있어서 s1.learn()이라고 써주면 된다

s2 = Student("이둘", 2)
print(f'{s2.name} 학생은 {s2.grade}학년입니다.')
s2.learn()