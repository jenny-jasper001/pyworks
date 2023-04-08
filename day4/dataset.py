#자료 구조 - 리스트, 딕셔너리, 튜플, 집합
#리스트에 과일이 있으면
fruit = ['사과', '바나나', '딸기', '바나나'] #리스트 - 순서가 정해져 있고 중복이 가능하다.
print(fruit) #대괄호로 출력
print(fruit[0])

fruit2 ={'사과': '빨강', '바나나':'노랑', '사과': '파랑'} #딕셔너리 - 찾고싶은거 찾는거
print(fruit2) #중괄호로 출력 #딕셔너리는 순서가 있고 키(사과, 바나나 같은거)는 중복 불가지만 값(빨강, 노랑, 파랑같은거)은 수정가능하다
print(fruit2['사과']) #인덱싱하면 빨강이 출력됨
for key, val in fruit2.items(): #items함수는 전체출력
    print(key, ':' , val) 

#튜플 - 괄호, 삭제가 안된다 , 순서가 있고 중복이 허용되지만 값의 수정과 삭제가 불가능하다
t = ('a', 'b', 'c', 'a')
print(t)
print(t[0]) #인덱싱은 대괄호[]로 한다

