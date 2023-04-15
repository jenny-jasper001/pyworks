# 바이너리 파일 쓰기 , 문서가 아닌 영상이나 음성일때
#파일 경로 - 상대 경로

with open('./output/data.bin', 'wb') as f:  #상대경로 일때 쓰는법 #bin 빈파일
    text = "오늘은 비가 내려요"
    f.write(text.encode())  #0과 1로 코드화하다

#print("파일을 쓸 수 없습니다.")
#bin 파일은 파이참에서 읽을수 있는데 c드라이브에서는 안 읽어져서 파일을 읽으려고함
with open('./output/data.bin', 'rb') as f:
    data = f.read()
    print(data)
    print(data.decode()) #encode되서 알아볼수 없게(16진수로된걸) decode로 해석하는것