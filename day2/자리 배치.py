
#좌석 배치 
customer = int(input("입장객 수 입력: ")) #입장객
col_num = int(input("좌석 열 수 입력: ")) #colum numer = 5 좌석이 5개
row_num = 0;  #줄수

if customer % col_num == 0:
    #row_num = int(customer / col_num)
    row_num = customer // col_num  #위에서 안하고 //로 바로 몫 구하기 
else:
    row_num = int(customer / col_num) + 1 #계산시 소수가 나오면 안되므로 정수가 되게 int
"""
#print(str(row_num)+ "줄이 필요합니다.")
print(f'{row_num}줄이 필요합니다.')
print("{}줄이 필요합니다.".format(row_num)) #format함수 
       #객체               #함수
#format 문자열 함수 .format
#print(f'{row_num}줄이 필요합니다.') = print("{}줄이 필요합니다.".format(row_num))
"""

for i in range(0, row_num):
    for j in range(1, col_num+1):
        #좌석번호가 고객 번호보다 클때 빠져나옴
        seat_num = (col_num * i ) + j
        if seat_num > customer:
            break
        #print("좌석"+ str(seat_num), end=' ')
        print(f'좌석{seat_num}', end="")
    print()
    
