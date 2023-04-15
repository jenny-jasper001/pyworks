 #영어 단어장 만들기
import random #값을 랜덤하게 출력되게 함

try:
    f = open("c:/pyfile/words.txt", 'r')
    #split(구분기호) - 공백문자로 분리 split() = split(" ")
    #리스트화 된다

    data = f.read().split(" ")   #split(" ")는 공백문자로 나누어준거다
    word = random.choice(data) #(data)는 리스트
    print(word)
    #print(data[3])  #words의 0,1,2,3번 즉 4번째에 있는 dog가 출력이 된다, 파이썬은 첫번째값을 0으로 센다
except:
    print("파일을 읽을 수 없습니다.")
