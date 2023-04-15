#파일 쓰기 - 생성, 파일 읽기
# open(파일의 경로, 모드)모드 - 쓰기 : 'w', 읽기 : 'r' (쓰기모드는 w, 읽기모드는 r이다)
f = open("c:/pyfile/test.txt", 'w') #pyfile에 test파일을 만들겠다
f.write("hello\n") #test.txt에 우리가 쓰는거 #\n 은 줄 나누기
f.write('감사합니다.\n')

#숫자쓰기는 안되므로 숫자 -> 문자화를 해야함 ''를 붙이거나 , 예) str(3,3)
f.write('12\n')
f.write(str(3.3)+'\n')
f.close() #pyfile에 test파일이 생기고 hello라 서져 있다.

