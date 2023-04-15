# 파일 리스트 읽기
try: #try: tab키로 4칸 들여쓰기 해줌 #try:~except로 오류날때 출력되는거 하기
    #f = open("c:/pyfile/daylist.txt", 'r')
    with open("c:/pyfile/daylist.txt", 'r') as f:  #:은 코드블락이므로 있으로 tab키로 4칸 들여쓰기 해주어야 한다.
        datalist = f.read()
        print(datalist)
        # f.close()
except:
    print("파일을 찾을 수 없습니다.")