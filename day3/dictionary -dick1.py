# dictionary 딕셔너리 생성과 사용
# 과일= {"딸기": 'red'}  -> {key:value}
fruit = {'딸기': 5000, 'banana': 3000, 'apple': 10000}
print(fruit)

fruit['감'] = 4000
print(fruit)

#모든 키 가져오기 keys() 함수사용, 키 - 딸기 banana apple같이 앞에 있는 값
print(fruit.keys())
print(list(fruit.keys())) #리스트로 만들때 

#모든 값 가져오기 - values(), value는 뒤의 5000,3000,10000값이 출력 
print(fruit.values())
print(list(fruit.values())) #리스트로 만들때

# value 출력
print(fruit['딸기'])

#전체 출력
for key in fruit:
    print(key, ':', fruit[key]) #key=과일 ,그리고 과일값을 출력하고 싶을때
    
    
#전체 출력 - items() :모든 키와 값을 가져오기
for key, val in fruit.items():
    print(key, ':', val)
