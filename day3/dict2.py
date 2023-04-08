#용어 사전
word = input('정의 되어 있는 단어를 입력하시오: ')
#dictionary를 dic이라 정의

dic = {
    "이진수" : "컴퓨터가 사용하는 0과 1로 이루어진 수",
    "버그" : "프로그램이 적절하게 동작하는데 실패하거나 발생하는 코드 조각",
    "알고리즘" : "어떤 문제를 해결하기 위해 정해진 일련의 절차", #새로 언어를 추가하려면 쉼표 필요
    "파이썬" : "쉽고 배우기 쉬운 객체지향 프로그래밍 언어"
}

#예외처리
try:
    definition = dic[word]
    print(definition)
except KeyError: #숫자는 Valueerror 문자는 Keyerror
    print("정의된 단어가 없습니다.")



