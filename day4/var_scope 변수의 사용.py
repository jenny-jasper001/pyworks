#변수의 사용(사용범위) - 한번 쓰고 말때 사용한다(지역변수)
#지역 변수는 - 함수나 제어문의 블럭 안에서 생성
#지역변수 소멸 - 함수나 제어문의 실행이 끝나면 소멸
def one_up(): #함수를 호출하고 나면 x가 사라진다
    x = 1 #이 함수의 지역 변수
    x = x + 1
    return x

# 메인 영역
#print(x) x값을 알고 싶은데 오류가 난다, 실행되고 return한 후 소멸한 x를 부르니 모르는 함수라고 한것, x가 변수 할당되지 않은것
print(one_up()) #2가 나온다
print(one_up()) #한번 더 호출해도 2가 나온다