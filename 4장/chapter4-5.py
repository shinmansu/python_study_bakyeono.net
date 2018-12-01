# 데이터 유형 확인하기
'''
이 장에서 데이터가 값과 유형으로 구성된다는 점과 파이썬의 기본 데이터 유형들을 배웠다.
유형이 무엇이냐에 따라 데이터에 적용할 수 있는 연산이 달라진다는 것도 여러 번 강조해 설명했다.
데이터 유형이 갖는 의미가 크기 때문에,어떤 데이터의 유형이 무엇인지 확인하거나 데이터 유형을
다른 것으로 변환하는 것도 자주 필요한 기능이다. 이 장의 마지막 내용으로 그 방법을 알아본다.
'''

# 4.5.1 데이터 유형 확인하기
# 데이터 유형을 확인하는 함수 type()

# print(type(10)) # 10 -> int(정수)
# print(type(1.0)) # 1.0 -> float(부동소수점 수)
# print(type(1+2j)) # 1+2j -> complex(복소수)
# print(type('?')) # ? -> str(문자열)
# print(type(True)) # True -> bool(불리언)
# print(type(None)) # None -> NoneType (None 유형)

# 매개변수를 확인해 다른 데이터 유형으로 변경하는 방식으로 진행

# number = input()
# print(number)
# number = int(number) # int로 데이터 타입을 전환하지 않으면 에러가 난다 str +1
# number + 1 # 문자 취급을 받을 때는 입력 받지 못한다
# print(int(1.01)) # 1만 출력 된다 (float -> int 변경)

# number = input()  # 사용자에게 텍스트를 입력받음
#
# print(int(number))      # 실수를 정수로 정수로 변환하면 오류가 발생한다
# '''만일 사용자로부터 입력받은 수가 정수가 아니라 실수라면, int() 함수 대신 float() 함수를 사용하면 된다.'''
# print(float(number))      # 실수로 변환하면 올바르게 변환된다
#
# print(float(10))         # 정수를 실수로 바꿀 때도 사용

# age = 17
# print('저는' + age '살입니다') #  오류 발생 must be str, not int
# #int 형은 str 과 합칠 수 없음
# #str을 추가해주면 된다
#
# age = 29
# print('저는 ' + str(age) + '살입니다')


'''정수(integer): int()
실수(floating point number): float()
복소수(complex number): complex()
문자열(string): str()
불리언(boolean): bool()
'''

'''
다음 프로그램의 오류를 찾아 수정하라.

number_1 = input()            # 사용자 입력 수 1
number_2 = input()            # 사용자 입력 수 2
result = number_1 + number_2  # 계산
print('결과: ' + result)      # 결과 출력
'''

# 정수를 입력받아 결과를 출력하는 함수
print('아래에 2개의 정수를 순서대로 입력해주세요.')
number_1 = int(input())
number_2 = int(input())
result = number_1 + number_2
print('결과: ' + str(result))

'''
4장 요약
데이터는 값과 유형으로 구성된다. 데이터의 유형에 따라 계산할 수 있는 연산이 다르다.
파이썬의 수 데이터 유형으로는 정수, 실수, 복소수가 있다. 실수를 다룰 때는 정밀도 오차 문제를 주의해야 한다. 
수 데이터 유형들은 같은 연산 방법을 공유한다.
파이선의 텍스트 데이터 유형은 문자열이다. 문자열에는 문자열을 위한 함수와 메서드들이 있다.
참과 거짓을 다루는 데이터 유형은 불리언이다. and, or, not 같은 불리언 연산을 이용해 더 복잡한 명제를 표현할 수 있다.
데이터의 유형을 확인할 때는 type() 함수를 사용하고,
데이터의 유형을 바꿀 때는 데이터 유형의 이름에 해당되는 함수(int(), float(), str() 등)를 사용한다.
'''