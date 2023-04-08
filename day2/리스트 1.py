# 리스트의 생성 및 인덱싱
seasons = ['봄', '여름', '가을', '겨울'] #리스트 생성
print(seasons[0]) #인덱싱
print(seasons[-1]) 


#리스트 전체 출력
print(seasons)   #

#인덱싱과 슬라이싱
print(seasons[0]) #인덱싱
print(seasons[1:3]) #슬라이싱

#전체 요소 출력
for i in seasons:
    print(i)

#리스트 요소의 개수를 세는 len함수
print('리스트(배열)의 크기', len(seasons))

# 요소를 수정하고 싶을 때
seasons[1] = 'summer'
print(seasons[1])
print(seasons)

#print(seasons)햐면 여름이 summer로 바꾸어져 나온다 ['봄', '여름', '가을', '겨울']->['봄', 'summer', '가을', '겨울']

#요소삭제 : del 명령어 사용
del seasons[1]
print(seasons)
# ['봄', '여름', '가을', '겨울']-> ['봄', '가을', '겨울']
