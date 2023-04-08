#리스트 생성 및 연산
score = [70, 80, 50, 90, 60]
print(len(score))
sum_v = 0

#유형 1 리스트
#총점 구할때
# i = score[0]
for i in score: #i가 score의 0번이다
    sum_v = sum_v + i #sum_v +=i
    print("i=", i)
print("총점: ", sum_v)

#평균 구할때
avg_v = sum_v / len(score) #평균 = 총점 / 개수

print("총점: ", sum_v)
print("평균: ", avg_v)


#유형 2 range score[i]를 쓴다
sum_v = 0 #앞에 sum에 값이 들어가서 다시 초기화 해준다
for i in range(0, len(score)):#0부터 len(score)까지
    sum_v += score[i]
print("총점: ", sum_v)


#유형 3 내장 함수 - sum()
print("총점: ",sum(score))













# 인덱싱 연습
print(score[0])
print(score[4])
print(score[-1])

#슬라이싱
print(score[0:]) #전체 쓸때 사용
print(score[1:3]) #  1부터 3까지 하나뺀거라 80, 50이 나온다
print(score[:-1]) #70 ,80 50,90
print(score[:]) #전체 쓸때 사용

