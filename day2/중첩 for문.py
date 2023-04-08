"""
# 중첩 for문
for i in range(5): #0,1,2,3,4 0~4까지 5번 돈다  range(5) = range(1,6) = range(0,5)
    for j in range(5):
        print('*', end='')
    print() # print()는 줄바꿈이다
    


*
**
***
****
*****  #행5개 
만들어보기

#행은 5개 위에서와 같이 range(5)는 그대로 쓰기


for i in range(5): #0,1,2,3,4 0~4까지 5번 돈다  range(5) = range(0,5)
    for j in range(0, i+1): #0을 넣으면 0+1은 1이므로 별을 1개 찍는다, 1을 넣으면 1+1은 2이므로 별을 두개 찍는다
        print('*', end='')
    print()


*****
****
***
**
*
위의 모양을 만드려고 아래의 식을 쓴다
for i in range(0, 5): #0번은 1번 회전했다
    for j in range(0, 5-i): 
        print('*', end='')
    print()


#1 2 3 4 5
#6 7 8 9 10
#11 12 13 14 15
#16 17 18 19 20
#만든다

i = 0 j = 1,2,3,4, -> 0+1 = 4*0+1
i=1 j= 5,6,7,8, -> 5 = 4*1+1
i=2 j= 9,10,11,12 -> 9 = 4*2+1
"""


for i in range(0, 4):
    for j in range(1, 5):
        num = (4*i)+j
        print(num, end=' ')
    print()
