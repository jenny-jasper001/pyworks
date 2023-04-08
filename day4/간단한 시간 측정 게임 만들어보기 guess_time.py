#속으로 20초를 세어 맞히는 프로그램
# "엔터를 누르고 20초를 셉니다"
# 20초가 지났다고 생각되면 엔터를 누른다

import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end - start
print(f'실제시간 : {et}초')
print(f'차이 : {abs(et-20)}') #abs 절대값 , -로 나오면 20초보다 덜 센거다 그래서 절대값을 쒸워준 겁니당