# Person 클래스 생성 한 다음에 상속 -> Employee 클래스 (상위)상속관계이다
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#상속 - 클래스 이름 (부모 클래스)
class Employee(Person):  #(Person)면 위의 Person을 상속받은거다
    def __init__(self, name, age, employee_id): #employee_id는 자기꺼 상속받은거 아님 자기꺼라 self로 씀
        super().__init__(name, age)  #부모의 멤버 생성(상속) - super()사용
        self.employee_id = employee_id #자신의 멤버 생성

    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 사번: {self.employee_id}')


p = Person("김강", 62) #부모
print(p.name)

#Employee 인스턴스 (emp) 를 사용
emp = Employee("김산", 31, 100)  #자신
emp.info()

