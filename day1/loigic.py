# 비교 연산 print를 붙여야 한다

x = 10
y = 11
print(x>y)
print(x == y)
print(x != y)
print(x is not y)

#논리 연산
 #비교연산을 or, and 를 사용해서 수행한다
x = 10
y = -10
# x,y 같이 
print(y)
print( x >0 and y>0) #and는 둘다 참일때 참이다 지금 친 값은 둘다 참이 아니므로 false가 나온다
"""#true and true --> true외에는 전부 false이다
#or 은 둘중 하나만 참이여도 참이다
# true or true -> true
true or false -> true
false or true -> true
not은 논리 부정(반대)
true -> false
false -> true
"""

print(x>0 or y>0)
print( not x>0 ) # not x>0은 x<0이라는 뜻이다 
