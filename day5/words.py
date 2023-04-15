#영어 단어장 만들어 보기 #동물 이름으로 만들어 보깅
try:
    words = ['ant', 'bear', 'chicken', 'dog', 'eagle', 'fox',
             'horse', 'lion', 'mouse', 'monkey', 'tiger']
    f = open("c:/pyfile/words.txt", 'w')
    for i in words:
        f.write(i + " ") #가로로 값을 출력시킨다
    f.close()
except:
    print("파일을 쓰는데 실패했습니다.")