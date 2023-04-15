# 이미지 파일 읽어와서(복사) 쓰기
try:
    with open("c:/pyfile/flower.jpg", "rb") as f1: #절대경로 - c드라이브에서 pyworks에 계속 들어요
        data = f1.read()   #rb로 읽었는데 뭘 읽었는지 모르니 print로 출력해보니 16진법으로 나옴
        #print(data) 이 데이터를 읽어보니 16진법이라 알아볼수 없는 형식이다


    #절대경로로 쓰면
    #c:/pyworks/day5/output/flower2.jpg

    with open("./output/flower2.jpg", "wb") as f2: #상대경로 - ./는 내파일과 output이 같이 있다는 뜻(output파일과 image file은 같은 위치에 저장되 있다)
        f2.write(data)          # ./(점이 한개이면 깉은 위치에 저장됨, 점이 2개이면 ../ 상위 폴더를 가리킨다)
    #그러므로 wb로 이진법이라 알아볼 수 없는 상태를 읽어줘서 jpg라는걸 알아차렸다
except:
    print("파일을 찾을 수 없습니다")

# "./output/flower2.jpg", "wb"에 flower2에 flower3, flower4로 숫자를 바꾸면 jpg가 복사가 되고 있다