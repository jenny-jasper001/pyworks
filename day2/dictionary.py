# dictionary 딕셔너리 - 리스트처럼 여러 개의 값을 저장할 수 있고,
# 키(key)와 값(value)으로 대응시켜 저장하는 자료구조이다.
# person = {'name':"김한국", "age":28}  name = key 김한국 = value
#리스트는 대괄호 딕셔너리는 중괄호 이다


person = {}  #빈 딕셔너리 선언

print(person)

#요소추가 리스트는 append를 쓴다
#딕셔너리 생성
person['name'] = "오상식"
print(person)
person['age'] = 35
person['phone'] = '010 -1111-2222'
print(person)

#특정 요소 출력
print(person['name']) #value는 키로 접근(인덱싱)한다 = key로 찾는다

# 전체 출력
for key in person:
    #person(person[key])
    print(key, ':', person[key])

#특정 요소 수정
person['age'] = 40
print(person['age'])

#특정 요소 삭제
del person['phone']
print(person)

#이메일 추가 (특정요소 추가)
person['email'] = 'test@test.co.kr'
print(person)
print(type(person))
#list는 type tab, 딕셔너리는 dict라고 나온다
