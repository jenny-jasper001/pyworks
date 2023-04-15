# 반복 쓰기
#f = open("c:/pyfile/repeat.txt", 'w')
with open("c:/pyfile/repeat.txt", 'w') as f: #:이 있으므로 tab키로 4칸 들여써야한다
    for i in range(1, 11):
        #f.write(str(i)) #숫자는 안되므롷 str(i)로 써주어야 한다
        data = f'{i}번째 줄입니다.\n' #f string
        f.write(data)


#f.close()


