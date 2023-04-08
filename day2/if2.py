"""
#조건문(if ~elif ~ else문) : 다중 조건문인 경우

pizza = input('피자가게가 열렸나요(예/아니오)?')
chicken = input('치킨가게가 열렸나요(예/아니오)?')

if pizza == '예':
    print('피자 가게로 가자')  #처음에는 일반 if 구문부터 써준다
elif chicken == '예':
    print('치킨가게로 가자')
else:  #pizza,chicken가 예가 아니라는 뜻이 숨겨져 있다 , pizza != yes
    print('편의점에서 라면을 먹자')
    


#근속년수가 5년이상이고 직급이 사원이면 대리로 승진
직급 = '사원'
근속년수 = 5

if 직급 == '사원' and 근속년수 >=5: #and는 둘다 참이야 true이다
    print("승진 대상입니다.") 
else:
     print("승진 대상이 아닙니다.")
"""

"
