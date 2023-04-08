"""
#리스트 연산
#합계, 평균, 개수 구하기
score = [70, 80, 50, 60, 90, 40] #학생 6명의 성적
count = len(score) #count라는 변수
sum_v = 0 # sum(70+80하는등 계속 변한다)을 구해야 해서 sum_v을 변수로 정의한것으로 0을 보통 많이 씁니다

for i in score: #score에 i가들어가면 값이 하나씩 나온다
    #sum_v = sum_v + i
    sum_v += i
    print("i =", i, "sum_v =", sum_v)

avg = sum_v / count #평균 구하는 법 평균 = 합계 / 개수
    
print("개수:", count)
print('합계:', sum_v)
print('합계:', avg)


#합계 구하는 내장 함수
print(sum(score))

print(max(score)) # 최댓값 구하기
"""

scorelist = [10, 20, 30, 40]

#요소 추가 (appen() 함수) -이때 추가된 값은 맨 뒤에 추가된다
scorelist.append(50)
print(scorelist)
#[10, 20, 30, 40, 50]

#특정 위치에 요소 추가(insert(위치번호, 값))
scorelist.insert(2, 60)  #두번째 자리에 60을 넣고 싶다
print(scorelist)
#[10, 20, 60, 30, 40, 50]


#요소 삭제(pop()) - 맨 뒤의 요소를 삭제한다
scorelist.pop()
print(scorelist)
#[10, 20, 60, 30, 40]

#요소의 개수 len함수
print(len(scorelist))
