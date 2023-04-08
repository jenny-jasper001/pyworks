pizza = input('피자가게가 열렸나요(예/아니오)?')
chicken = input('치킨가게가 열렸나요(예/아니오)?')

if pizza == '예':
    print('피자가게로 가자')  #처음에는 일반 if 구문부터 써준다
elif chicken == '예':
    print('치킨가게로 가자')
else:  #pizza,chicken가 예가 아니라는 뜻이 숨겨져 있다 , pizza != yes
    print('편의점에서 라면을 먹자')
