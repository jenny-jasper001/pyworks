# 타이핑 게임 만들기
# 영어 타자 게임 - 외부파일(단어장)
import random, time
try:
    f = open("c:/pyfile/words.txt", "r")
    data = f.read().split()   #split()은 공백을 준다
    word = random.choice(data) #질문이 word이다
    #print(word)
    f.close()

    n = 1 #문제의 번호
    input("[타자 게임] 준비되면 엔터!")
    start = time.time()  #현재까지의 시간(시작시간)
    while n <= 10:    #while 문
        question = random.choice(data)
        print(f'문제 {n}')
        print(question)
        user = input()  #게이머(내가, 컴퓨터가 아니라) 입력 하는거 #input이 나오면 계속 반복하는게 아니라 멈춘다
        if question == user: # 오타가 없으면 맞는것(타이핑 말하는거임)
            print("통과")
            n = n + 1 #문제 번호 1증가, 문제1, 문제2, 문제3....문제10까지

        else:
            print("오타, 다시 도전!")
    end = time.time()    #종료시간       #.2f 소수 둘째 자리까지
    print(f'게임 소요 시간 : {end - start:.2f}초')  #게임 소요 시간 종료시간(end) - 시작시간(start)

except:
    print("파일을 찾을수 없습니다.")