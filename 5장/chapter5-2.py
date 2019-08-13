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
# print(alphabet_list[::2])   # 전체 범위에서 두 요소마다 하나씩 선택
#
# print(alphabet_list[1::2])  # 1 이상의 범위에서 두 요소마다 하나씩 선택
#
# print(alphabet_list[::-1])  # 전체 범위에서 뒤에서부터 한 요소마다 하나씩 선택
#
#
# original_list = ['a', 'b', 'c', 'd']
# copied_list = original_list[:]
# print(copied_list == original_list)
#
# copied_list[0] = 'A'
# print(copied_list)
#
# print(copied_list == original_list)
#
# assigned_list = original_list    # 리스트를 다른 변수에 대입
# assigned_list[1] = 'B'           # 대입한 리스트를 수정
# print(original_list)                    # 원본 리스트의 내용이 변경되었다
#
# #변수로 바로 지정해주면 동일한 값이 되기 때문에 그 값을 변경할 때 오리지널 리스트도 바로 변경이 되어버림
#
# #범위를 지정하여 수정하기
# number_list[1:3] = [200, 300]
# print(number_list)
#
# #통계 함수
# #sum() 함수를 사용하면 시퀀스의 모든 요소의 합을 구할 수 있다
# print(min(number_list))
# print(max(number_list))
# print(min(['가','나','다'])) # 가장 작은 요소 (가나다순 비교)
# print(max(['가','나','다']))
#
# #  min([1, 2, 3, 'a'])   # 잘못된 크기 비교
# # TypeError: '<' not supported between instances of 'str' and 'int'

'''
center() 함수를 정의하라. 이 함수는 시퀀스를 하나 입력받는다. 
입력받은 시퀀스의 요소의 개수가 홀수이면 정가운데에 있는 요소를 반환한다.
그리고 요소의 개수가 짝수이면 가운데 요소 두 개를 리스트에 담아 반환한다.
함수를 호출한 예는 다음과 같다.

>>> center(['가', '나', '다', '라', '마'])
'다'

>>> center([2, 4, 8, 16, 32, 64])
[8, 16]
'''

def center(list=[1,2,3,4,5]):
    length = len(list)
    half = length//2
    if len(list)%2 == 0:
        center_list = list[half-1:half+1]
    else:
        center_list = list[half]
    return center_list

print(center([1,2,3,4]))

# def mirror(list=[1,2,3,4,5]):
#     mirror_list = list[len(list)-2::-1]
#     return list+mirror_list
#
# print(mirror())
#mirror 함수
'''
mirror() 함수를 정의하라. 이 함수는 시퀀스를 하나 입력받아 
그 시퀀스를 뒤집은 시퀀스를 원본에 덧붙여 반환한다.
단, 원본 시퀀스의 마지막 요소는 덧붙이지 않는다. 함수를 호출한 예는 다음과 같다.
'''
# print(mirror(['가','져','가','라']))


'''
연습문제 5-4 최대최솟값

minmax() 함수를 정의하라. 이 함수는 전달받은 시퀀스의 최솟값과 최댓값을 리스트에 담아 반환한다. 함수를 호출한 예는 다음과 같다.

>>> minmax([92, -21, 0, 104, 51, 76, -92])
[-92, 104]

>>> minmax(['파', '이', '썬', '프', '로', '그', '래', '밍'])
['그', '프']
'''

# def minmax(list = [1,2,3,4]):
#     min_list=min(list)
#     max_list=max(list)
#     min_max_list = [min_list,max_list]
#     return min_max_list
#
# print(minmax())

def mean(list=[1,2,3,4]):
    '''리스트를 전달받아 그 리스트 수의 평균을 출력하는 함수,
    갯수가 0개일 때는 None을 출력하게 한다. '''
    if len(list) != 0:
        list_mean = sum(list[:]) / len(list)
    else:
        list_mean = 'None'
    return list_mean

print(mean())


'''
시퀀스 조작 메서드 
시퀀스를 조작할 때 많이 사용되는 메서드 몇 가지를 알아보자. 
지금 소개하는 메서드는 시퀀스의 내용을 수정하는 메서드이기 때문에 
튜플 등의 불변 시퀀스에는 적용할 수 없으며, 가변 시퀀스인 리스트에 주로 사용된다.

메서드	용도
append(x)	요소 x를 시퀀스의 끝(오른쪽)에 추가한다
insert(i, x)	요소 x를 시퀀스의 i 위치에 삽입한다
extend(seq)	대상 시퀀스를 시퀀스의 끝에 연결한다.
pop()	시퀀스의 마지막 요소를 꺼낸다.
remove(x)	시퀀스에서 요소 x를 찾아 처음 발견된 것을 제거한다.
clear()	시퀀스의 모든 요소를 제거한다
'''

numbers = [10,20,30,40]
numbers.append(100)
print(numbers) # 100이 추가된 것을 알 수 있다



numbers.insert(4,50) # 시퀀스의 4번 위치에 50을 삽입
print(numbers)

numbers.extend([101, 102, 103])  # [101, 102, 103] 을 연결한다.
print(numbers)

#extend() 메서드는 += 연산으로 대신해도 된다.
numbers += [104, 105]  # numbers.extend([104, 105]) 와 동일
print(numbers)
print(numbers.pop())  # 마지막 요소를 꺼내 확인하고 버린다
print(numbers.pop())
print(numbers.pop())
print(numbers)

numbers.remove(40)  # 40을 찾아 삭제
print(numbers)

# 데이터를 찾을 수 없는 경우 오류 발생

numbers.clear()
print(numbers)


stations = []
stations.append('서울')
stations += (['수원', '대전'])
stations.extend(['밀양', '부산'])
stations.insert(3, '동대구')

print(stations)                 # 출력 1
print(stations.pop())           # 출력 2
print(stations.remove('수원'))  # 출력 3
print(stations)                 # 출력 4

name_list = []
phone_list = []

name_list.append('박연오')
phone_list.append('01012345678')
name_list.append('이진수')
phone_list.append('01011001010')
len(name_list)

print(name_list[0] + ' ' + phone_list[0])


'''
컬렉션을 사용함으로써 직접 변수를 정의할 필요가 없어졌고, 데이터를 더 유연하게 관리할 수 있게 되었다. 아직 이름 목록과 전화번호 목록이 하나의 연락처 목록으로 합쳐지지 못하고 구분되어 있다는 점이 신경쓰인다. 이 문제점은 5.4절에서 해결해 볼 것이다.
'''

'''
튜플은 구성요소를 변경할 수 없는 불변 데이터다. 연락처 목록처럼 수시로 데이터를 변경해야 하는 데이터는 튜플이 아니라 리스트로 작성해야 한다. 튜플은 데이터를 나열하되 그 순서나 내용이 변하지 않을 때 잘 어울린다. 예를 들어, 한 주의 요일 목록(일월화수목금토)은 변하지 않는 개념이므로 튜플로 표현하기에 적합하다.

코드 5-28 한 주를 구성하는 요일을 튜플로 정의

'''

days = ('일', '월', '화', '수', '목', '금', '토')  # 튜플 정의하기

print(days)

print(len(days))    # 길이 세기

print(days[0])  #     인덱싱 연산


print(days[::-1])   # 슬라이싱 연산 (새 튜플 생성)

print(days + ('천', '해', '명'))  # 시퀀스 연결 (새 튜플 생성)

'''
>>> days[1] = '月'     # 요소 대입: 지원하지 않음!
TypeError: 'tuple' object does not support item assignment

>>> days.append('천')  # append 메서드: 지원하지 않음!
AttributeError: 'tuple' object has no attribute 'append'
'''


'''
인지 표현하기
레인지를 표현할 때는 range() 함수를 사용한다. 
이 함수에는 매개변수를 1개 또는 2개 또는 3개 지정할 수 있다. 
지정하는 매개변수의 수에 따라서 생성되는 레인지가 다음과 같이 차이가 있다.

range(종료): 0 부터 종료값에 이르기 전의 1씩 증가하는 등차수열 시퀀스를 생성한다.
range(시작, 종료): 시작값부터 종료값에 이르기 전의 1씩 증가하는
등차수열 시퀀스를 생성한다.
range(시작, 종료, 간격)) 시작값부터, 종료값에 이르기 전의 간격만큼씩
증가하는 등차수열 시퀀스를 생성한다.
'''

print(list(range(9)))         # 0 이상, 9 미만의 1씩 증가하는 등차수열

print(list(range(5, 12)))     # 5 이상, 12 미만의 1씩 증가하는 등차수열


print(list(range(0, 20, 2)))  # 0 이상, 20 미만의 2씩 증가하는 등차수열

print(range(9))# 내용 대신 range(0, 9)라는 표현만 출력된다

#레인지의 내용을 확인하려면 list() 함수나 tuple() 함수로 감싸 레인지를 리스트나 튜플로 변환해주어야 한다.

print(list(range(9)))
print(tuple(range(9)))

경 = 10 ** 16
print(range(경))
# print(list(range(경)))#메모리 에러 발생 너무 큰 수를 출력할 수 없음
print(range(경)[-1]) #요소는 출력 가능

print(range(0, 100, 2)[10])       # 인덱싱 연산


print(range(0, 100, 2)[10:20:2])  # 슬라이싱 연산 (새로운 규칙 생성)


# range(0, 100, 2)[10] = 50  # 요소 대입은 지원하지 않는다.

'''
레인지를 리스트로 변환한 후에는 수정 가능하다 
'''

numbers = list(range(10))
numbers[5] = 100
print(numbers)


'''연습문제 5-7 레인지로 계산하기

레인지를 사용해, 0 이상 10000 미만인 모든 짝수의 합계를 구하라'''
range(1000)
print(list(range(1000))[999])

print(sum(range(1000)))
'''
연습문제 5-8 레인지로 리스트 생성하기

레인지를 사용해, 9부터 0(포함)까지 거꾸로 나열한 리스트를 생성하라.

힌트: 레인지를 리스트로 변환하는 것을 잊지 말자
'''

print(list(range(9,0,-1)))


'''문자열은 시퀀스이므로 시퀀스 연산이 가능하다. 그러나 불변 데이터이기 때문에 내용을 수정하는 것은 허용되지 않는다.

코드 5-36 문자열의 시퀀스 연산

>>> message = '사막이 아름다운 것은 어딘가에 물을 감추고 있기 때문이야'
>>> '물' in message     # 요소가 들어있는지 확인
True

>>> message[17]         # 인덱싱 연산
'물'

>>> message[:2]         # 슬라이싱 연산
'사막'

>>> message[17] = '샘'  #  요소 수정은 불가하다
TypeError: 'str' object does not support item assignment
'''

#문자열을 튜플, 리스트로 변화시키기
print(list('파이썬'))

print(tuple('일월화수목금토'))

'''
연습문제 5-9 시퀀스 뒤집기

시퀀스를 입력받아 반대 순서로 뒤집어 반환하는 함수 reverse()를 정의하라. 그 후, 이 함수에 리스트, 튜플, 레인지, 문자열을 각각 입력해 결과를 확인해 보아라. 예를 들면 다음과 같다.

>>> reverse([10, 20, 30, 40])
[40, 30, 20, 10]

>>> reverse(tuple('일월화수목금토'))
('토', '금', '목', '수', '화', '월', '일')

>>> reverse(range(10))
range(9, -1, -1)

>>> reverse('파이썬 프로그래밍')
'밍래그로프 썬이파'
'''

def reverse(sequence =  [1]):
    """시퀀스(리스트,튜플,레인지)를 입력 받아 그 시퀀스를 역순으로 출력하는 함수"""
    if type(sequence) == list:
        reverse_sequence = sequence[::-1]
    elif type(sequence) == tuple:
        reverse_sequence = sequence[::-1]
    elif type(sequence) == range:
        reverse_sequence = range(len(sequence),-1,-1)
    else:
        reverse_sequence = str(type(sequence)) + '는 출력이 불가능합니다.' + 'list,tuple,range 타입으로 다시 입력해주세요'
    return reverse_sequence

print(reverse(1))
