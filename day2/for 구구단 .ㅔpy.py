#구구단

dan = int(input("단을 입력하세요: "))
result_val = ""
for i in range(1, 10):
    #이스케이프 문자 - '\n' (줄바꿈)
    current_val = f'{dan} x {i} = {dan * i}\n'
    result_val = result_val + current_val 
print(result_val)
#전체 구구단 행렬을 알아야한다

"""

#전체 구구단(2~9단)
#교재 푸는 방법으로 풀기
start_dan = int(input("시작단 입력: "))
end_dan = int(input("끝단 입력: "))

for i in range(start_dan, end_dan+1):  #range(1,4)는 1,2,3이다 4-1해준다 그래서 만약에 시작단 1 끝단 5를 원한다면 (시작단, 끝단+1)를 해주어야 한다
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print()
 
"""





