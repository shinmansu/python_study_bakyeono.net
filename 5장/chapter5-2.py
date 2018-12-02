#5.2 시퀀스
'''
5.2.1 순서가 있는 데이터 구조

시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열한 것이다. 다음은 장바구니에 담을 물건을 메모한 목록이다.

아이스크림, 커피, 설탕, 쿠키, 우유

순서대로 아이스크림이 첫 번째 ,커피가 두 번째 식으로 나열되는 데이터이다

네 번째로 주분한 상품은 쿠키이다

시퀀스의 특징

데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조다.
특정 위치(~번째)의 데이터를 가리킬 수 있다.
'''

'''
하지만 시퀀스 속의 데이터에 어떤 정렬 규칙이 반드시 있어야 하는 것은 아니다.
위 날짜 시퀀스 뒤에 ‘1999-12-31’ 같은 과거의 날짜가 들어갈 수도 있고,
심지어 날짜가 아니라 ‘아이스크림!’ 같은 데이터가 들어갈 수도 있다. 
시퀀스에 담은 데이터의 순서란 데이터의 나열 순서일 뿐이다.
순서가 있다는 것과 정렬되었다는 것은 의미가 다르다.
시퀀스의 데이터는 어떤 기준에 따라 정렬되었을 수도 있고 무작위로 나열되었을 수도 있다. 
어쨌든 데이터를 관리하기 위한 순서(번호)는 반드시 존재한다.
'''

'''
시퀀스 컬랙션의 종류 

파이썬은 리스트(list), 튜플(tuple), 레인지(range),
문자열(string) 등이 여러 가지 시퀀스 컬렉션을 제공한다. 
이 시퀀스들은 데이터를 저장하고 표현하는 방식이 서로 다르지만, 
요소에 번호를 붙여 순서대로 관리한다는 점은 모두 똑같다.
'''

#5.2.2 리스트

'''
목록이라는 뜻으로 파이썬 시퀀스 중에서 가장 많이 사용되며 가장 대표적이다 
리스트는 대괄호([, ])를 이용해 표현할 수 있다. 다음은 몇 가지 리스트의 예다.
'''

#리스트 표현하기
# ❶ 빈 리스트
[]

# ❷ 여러 유형의 데이터로 구성된 리스트
[10, 'hi', True]

# ❸ 숫자로 구성된 리스트
[1, 2, 3, 4]

number_list = [1, 2, 3, 4, 5]
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

'''
컬렉션의 이름 짓기

컬렉션의 이름을 지을 때는 원자 데이터의 이름과 구별되도록 하는 것이 좋다. 복수형 이름이나 컬렉션의 종류를 접미사로 붙이는 방식이 많이 사용된다.

복수형 이름: numbers, names 등
컬렉션의 종류를 접미사로 붙이기: _list, _dict, _set 등
'''

print(number_list[0])


'''
연습문제 5-1 수 리스트 정의하기

0 이상이고 100 미만인 모든 8의 배수의 리스트 multiples_of_8_list를 정의하라.

힌트: 요소를 직접 계산해서 나열하기가 불편할 것이다.
이후에 배울 레인지를 사용하면 그런 불편이 줄어든다.

'''
#
# multiples_of_8_list = [8,16,24,32,40,48,56,64,72,80,88,96]

#5.2.3 시퀀스 연산


'''
소속 검사하기
시퀀스에 어떤 요소가 들어 있는지 확인하고 싶을 때는 in 연산자를 사용한다.
반대로 요소가 없음을 검사하려면 not in을 사용한다.
'''
#
# print(3 in number_list)       # number_list에 3이 들어 있는지 검사
# print('z' in alphabet_list)   # alphabet_list에 'z'가 들어 있는지 검사
# print(0 not in number_list)   # number_list에 0이 안 들어 있는지 검사
#
# print(len(number_list))
#
# print(len(alphabet_list))

# 시퀀스의 연결과 반복

print(number_list + alphabet_list)  # 리스트 연결하기

print(number_list * 2)              # 리스트 반복하기

'''
컬렉션에 들어 있는 특정 요소를 가리키는 것을 인덱싱(indexing) 연산이라고 한다.
시퀀스에서는 구하려는 요소의 인덱스(index, 항목의 위치 번호)를 이용해 인덱싱한다. 
다음 예는 alphabet_list에서 1번 위치와 -1번 위치의 데이터를 구하는 예다.
'''
#
# print(alphabet_list[1])   # 1번 위치(두 번째)의 요소 가리키기
#
# print(alphabet_list[-1])  # -1번 위치(뒤에서 첫 번째)의 요소 가리키기
#
#
# number_list[2] = -3
#
# print(number_list)

'''
가변 데이터와 불변 데이터

데이터 유형은 내용의 수정이 허용되는 것과 금지되는 것으로도 분류가 된다.

리스트는 값을 변경할 수 있는 가변(mutable) 데이터다.
number_list[2] = '-3'처럼 내용을 수정하는 연산이 가능하다.

반면, 값을 변경할 수 없는 불변(immutable) 데이터도 있다. 
불변 데이터에는 수, 튜플, 문자열 등이 있다. 
number = 10을 저장한 후 number += 1을 실행하면 number의 값은 11로 변한다. 
하지만 number가 가리키는 값이 바뀌었을 뿐, 10이 11이 된 것은 아니다.
'''

'''
슬라이싱: 범위를 정해 선택하기
인덱싱 연산은 단 하나의 요소만을 가리키지만, 
슬라이싱(slicing) 연산을 이용하면 일정한 범위의 요소를 선택할 수 있다.
슬라이싱 연산으로 선택할 범위를 지정할 때는 
대괄호 속에 속에 콜론(:) 연산자로 시작 위치와 종료 위치를 구분해 표기한다.
이 때, 시작 위치는 범위에 포함되지만 종료 위치는 포함되지 않는다.
(시작 위치 <= 범위 < 종료 위치)
'''
#
# print(alphabet_list[2:6]) # 2 이상 6 미만 위치의 범위 선택
# print(alphabet_list[:3]) # 3 미만 위치의 범위 선택 (시작 위치 생략)
# print(alphabet_list[5:]) # 5 이상 위치의 범위 선택 (종료 위치 생략)
# print(alphabet_list[:] ) # 전체 범위 선택 (시작, 종료 위치 모두 생략)
#

'''
슬라이싱 간격 지정 

슬라이싱 연산을 표현할 때 대괄호 안에 세 번째 값으로 간격(step)을 지정할 수 있다.
간격은 몇 번째 요소마다 하나씩 선택할 것인지를 뜻한다. 
예를 들어 간격을 2로 지정하면 두 요소마다 하나씩 선택한다. 
간격이 음수이면 뒤에서부터 역방향으로 선택한다.
'''
print(alphabet_list[::2])   # 전체 범위에서 두 요소마다 하나씩 선택

print(alphabet_list[1::2])  # 1 이상의 범위에서 두 요소마다 하나씩 선택

print(alphabet_list[::-1])  # 전체 범위에서 뒤에서부터 한 요소마다 하나씩 선택
