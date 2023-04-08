"""
# 반복문(while무한반복) while1파일은 무한반복 아닌거임
#1부터 10까지 출력

n = 0
while True:
    n = n + 1
    if n > 10:
        break
    print(n)
#0~9까지는 false라 출력되고 10은 true라 break에 걸려 출력이 끝난다
"""

#반복구문에서 'y' 이면 "반복을 계속합니다"
#'n'이면 "반복을 중단합니다."
# 'y', 'n' 둘다 아니면 "정상 답변이 아닙니다."
#조건이 3개이므로 if,elif,else를 쓴다

while True:
    key = input("반복을 계속 할까요(y/n)?")

    if key == 'y' or key == 'Y':
        print("반복을 계속합니다.")
    elif key == 'n' or key == 'N':
        print("반복을 중단합니다.")
        break
    else:
        print("정상 답변이 아닙니다.")
