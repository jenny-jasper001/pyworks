# 절대값을 계산하는 함수

def myabs(x): #-1이 x에 들어간다
    if x < 0:
        return -x #절대값이 1이 나와야 하므로 -(-1)해야햐서 -쓴다
    else: #x가 0보다 크다
        return x #그냥 1로 나옴

print(myabs(4))
print(myabs(-1)) #1이 나옴
print(abs(-1))

#1~30까지 자연수의 자연수 중 3의 배수를 출력하시오, 배수의 개수 구하기
#def = define
def times(x):
    for i in range(1, 31):
    #pass #오류 날꺼 같으면 pass써놓으면 오류가 안난다
        if i % x == 0: #3으로 나누어 떨어지는 수(나머지가 0인것)
            print(i, end=' ')
times(3)

"""
i = 1, 1 % 3 == 0 false
i = 2, 2 % 3 == 0 false
i = 3, 3 % 3 == 0 true 3이 true
i = 4, 4 % 3 == 0 false
i = 5, 5 % 3 == 0 false
i = 6, 6 % 3 == 0 true 3,6이 true
i = 7, 7 % 3 == 0 false
"""

times(3)
