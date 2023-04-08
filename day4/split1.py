#문자열을 구분해서 리스트로 생성한 함수
# split(구분기호)
f = "banana, grape, kiwi"
print(f.find(' ')) #공백 문자는 숫자이다, 쉼표 다음이 7이니까 7이 나온다
f = f.split(',') #(' ') 한칸 띄면 공백으로 본다, 비어있는게 공백 문자라는 뜻이다
print(f)
print(f[1])

#문자를 수정(변경)시키는 함수 - replace(변경전, 변경후)
str1 = "Hello World"
str1 = str1.replace("World", "Korea") #World를 Korea로 바꾸어준다
print(str1)

#문자열의 공백 처리 함수 - strip()
str2 = " hi, soo"
str2 = str2.strip() #왼쪽 오른쪽 공백 처리
str2 = str2.lstrip()  #왼쪽을 공백처리
print(str2)

# 찾는 문자열의 위치를 찾는 함수 - data를 가져올대 사용 find()- 결과가 숫자(index)로 나온다
#몇번 index인지 나온다
msg = "Hello"
print(msg.find('H')) #0번에 있다고 나옴 #대소문자를 구분한다
print(msg.find('l')) #첫번째 l을 찾음 - 2를 출력
print(msg.find('k')) # -1 (찾는 문자가 없으면 -1을 반환한다)