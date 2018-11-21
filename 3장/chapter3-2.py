#함수 호출하기

import math

'''
함수를 호출하면 다음 순서로 함수가 실행된다.

괄호 속의 데이터가 함수에 전달된다.
함수 본문의 파이썬 코드가 위에서 아래로 차례대로 실행된다.
함수가 끝나면 함수 실행이 종료되고, 함수의 실행 결과가 반환된다. 

알아 두기

함수 호출하기: 함수이름()
함수에 데이터를 전달하여 호출하기: 함수이름(데이터)
함수를 호출하여 반환된 값을 보관하기: 결과 = 함수이름(데이터)
함수를 호출하여 반환값을 화면에 출력하기: print(함수이름(데이터))

'''

print('수를 입력해 주세요')
number = int(input())

result = round(math.sqrt(number * math.pi))
print('계산 결과:', result)