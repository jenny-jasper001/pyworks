# 성적 통계 - 리스트 딕셔너리 둘다 가능한데 딕셔너리가 편함
# 4명의 학생의 국어 영어 수학 점수
#리스트안에 딕셔너리가 요소로서 존재하고 있다
student = [
    {'name':'이대한', 'kor':80, 'eng':80, 'math':75}, #중괄호 딕셔너리, 대괄호 리스트
    {'name':'박민국', 'kor':70, 'eng':65, 'math':60},
    {'name':'오상식', 'kor':75, 'eng':70, 'math':50},
    {'name':'최지능', 'kor':70, 'eng':90, 'math':90},
]
print("=== 학생의 성적표 ===")
print(" 이름 국어 영어 수학") #제목 만들어 주기
for std in student: #student를 std로 줄이기 student가 변수로써 반복하는 애이다
    #print(std['name'], std['kor'], std['eng'], std['math'])
    print(f'{std["name"]} {std["kor"]} {std["eng"]} {std["math"]}' ) #바깥이 '이므로 안은 "을 해준다

#개인의 총점 별점 구하기
#총점만 구한상태
print("=== 개인별 총점과 평균 ===")
print("이름 총점")
for std in student: #이대한 부터 박민국까지 반복한다
    total = std["kor"] + std["eng"] +std["math"] #이대한 = 80+80+75
    avg = total / 3 #평균
    print(f'{std["name"]} {total} {avg:0.2f}') #0.2f소수점 둘째자리까지 , 0.1f 첫째 자리까지, 0.3f는 셋째자리까지임
#f sting 사용