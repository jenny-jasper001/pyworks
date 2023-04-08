#나이를 계산해주는 프로그램
#태어난 년도를 입력받아 나이를 출력하는 기능


#나이계산 = 현재년도 - 태어난년도 + 1
# 현재 년도 (변화 없음) 태어난 년수(변수)
현재년도 = 2023 #현재년도 뛰어쓰기 하면 안된다 변수는 뛰어쓰기 안됨
태어난년도 = int(input("태어난 해를 입력하세요. "))
나이 = 현재년도 - 태어난년도 + 1
print("나이는" + str(나이) + "세입니다.")


#태어난년도 = input("태어난 해를 입력하세요. ")로 계산하면 에러가 난다
#나이 = 현재년도 - 태어난년도 + 1
#input("태어난 해를 입력하세요. ")는 문자이기 때문에 나이 = 현재년도 - 태어난년도 + 1는 숫자이므로문자와 계산불가 숫자는 서로 뺄수가 없다 그래서 int()함수로 int(input("태어난 해를 입력하세요. "))해서
#문자를 숫자로 바꾸어 주어야 한다

"""
계절 = '봄'
계절
'봄'
사계절 = ['봄', '여름', '가을'. '겨울']
SyntaxError: invalid syntax
사계절
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    사계절
NameError: name '사계절' is not defined. Did you mean: '계절'?
사계절 = ['봄', '여름', '가을'. '겨울']
SyntaxError: invalid syntax
사계절[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    사계절[0]
NameError: name '사계절' is not defined. Did you mean: '계절'?
사계절 = ['봄', '여름', '가을', '겨울']
사계절
['봄', '여름', '가을', '겨울']
사계절[0]
'봄'
사계절[2]
'가을'
사계절[0:2]
['봄', '여름']
"""
