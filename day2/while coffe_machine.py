#커피 자동판매기 프로그램
coffee = 5

#돈 넣는 건 계속 반복
while True:
    try:
        money = int(input("돈을 넣어주세요: ")) #int함수로 전체 숫자로 변경해준    
        if money == 400: #커피 가격은 400원
            print("커피가 나옵니다")
            coffee = coffee -1 #커피를 팔아서 커피의 수량이 줄어든다 #coffee -=1
        elif money > 400:
        #print("커피가 나오고, 거스름돈 "+ str(money-400) + "원입니다.")
            print(f'커피가 나오고, 거스름돈 {money-400}원입니다') #f String 방식
        #print('커피가 나오고, 거스름돈 {}원입니다'.format(money-400))
            coffee = coffee - 1 #coffee -= 1  
        else:  #coffee가 400원 이하일때
            print("커피가 나오지 않습니다.")
    #print("남은 커피의 양은 ", str(coffee) , "개입니다.")
        print(f"남은 커피의 양은 {coffee}개입니다.") #4칸씩 맞추어주는데 이걸 밖으로 뺀다
    #커피의 개수가 0이되면 반복중단이다
        if coffee == 0:
            print("커피가 모두 소진되었습니다, 판매를 중지합니다.")
            break
    except:
        print("숫자를 입력하시오")
