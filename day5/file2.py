#파일 일기, 예외 처리(오류 처리)
try: #:밑으로 4칸 들여쓰기 해야함, tab키로 한꺼번에 4칸 들여쓰기 가능
    f = open("c:/pyfile/test.txt", 'r') #외부 파일을 파이썬에 읽는것 r
    data = f.read()
    print(data)
    f.close()
except: #test가 맞는데 실수로 text가 나오면 오류가 아니라 파일을 찾을 수 없다고 안내해줌
    print("파일을 찾을 수 없습니다.")