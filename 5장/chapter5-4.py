#집합

'''
집합의 특징

순서나 키 없이, 포함되는 원소를 모아 둔 데이터 구조다.
원소를 중복으로 저장하지 않는다.
합집합, 교집합 같은 수학의 집합 연산이 가능하다.
어떤 원소가 집합에 포함되었는지 검사할 수 있다.
'''
'''
원소가 하나인 집합

{원소1, 원소2, 원소3, …}

공집합

set()  # 빈 딕셔너리는 {}로 표현하도록 약속되어 있음!

'''

# 정수의 집합
int_set = {0, -127, 97, 1789}

# 이메일 주소의 집합
email_set = {'bakyeono@gmail.com', 'i@bakyeono.net'}

# 공집합
empty_set = set()


'''
연습문제 5-13 집합 정의하기

다음 세 집합을 각각 파이썬 코드로 정의하라.

* 한 주의 모든 요일
* 여러분이 학교나 직장에 가는 요일
* 여러분이 휴식을 취하는 요일
'''

all_day = {
    'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'
}

all_work_day = {
    'Monday','Tuesday','Wednesday','Thursday','Friday'
}

all_weekend_day = {
    'Saturday','Sunday'
}

print(set([6, 1, 1, 2, 3, 3, 1, 5, 5, 4]))
print(set(('사과', '토마토', '바나나', '감')))

#코드 5-61 레인지를 이용해 집합 정의하기
짝수 = set(range(0, 10000, 2))
홀수 = set(range(1, 10000, 2))

print(짝수)

'''
시퀀스에서 중복된 원소 제거하기
시퀀스의 중복 원소를 제거할 때 집합 변환을 활용할 수 있다. 
시퀀스를 집합으로 변환했다가 다시 시퀀스로 변환하면 된다.
단, 이 방법을 사용할 때는 중복 원소뿐 아니라 원소의 순서라는 중요한 정보가 함께 사라진다는 점에 유의해야 한다.
'''

print(list(set([6, 1, 1, 2, 3, 3, 1, 5, 5, 4])))
[1, 2, 3, 4, 5, 6]


'''
연습문제 5-14 중복 없이 시퀀스 합치기

0 이상 1000 미만의, 3의 배수 또는 4의 배수는 모두 몇 개인지 계산하라.

힌트: 레인지, 리스트, 집합을 모두 활용하자.
'''

three_or_four_count = len(list(range(0,1000,3))+list(range(0,1000,4)))-1

print(three_or_four_count)

들짐승 = {'사자', '박쥐', '늑대', '곰'}
날짐승 = {'독수리', '매', '박쥐'}
바다생물 = {'참치', '상어', '문어 괴물'}

print(len(들짐승))

'''
소속 검사하기
어떤 원소를 포함하는지 확인하는 것은 집합의 핵심 기능이다. 시퀀스에서 요소를 검사할 때, 그리고 매핑에서 키를 검사할 때처럼 in과 not in 예약어를 이용해 원소를 검사할 수 있다.

코드 5-65 집합에서 소속 검사하기

>>> '늑대' in 들짐승
True

>>> '곰' not in 들짐승
False
'''

#교집합

짐승 = 들짐승.union(날짐승)  # 들짐승과 날짐승의 합집합
print(짐승)

짐승 = 들짐승 | 날짐승 | {'인간'} #합집합 시프트 \ 키

print(짐승)

#합집합
들짐승_날짐승 =  들짐승.intersection(날짐승)  # 들짐승과 날짐승의 교집합
print(들짐승_날짐승)

들짐승_바다생물 = 들짐승.intersection(바다생물)  # 짐승과 바다생물의 교집합
print(들짐승_바다생물)
들짐승_바다생물 = 들짐승 & 날짐승 # 교집합

#차집합
들짐승_차_날짐승 = 들짐승.difference(날짐승) #들짐승에서 날짐스에 포함된 항목들을 제외한 집합
print(들짐승_차_날짐승)

날짐승_차_들짐승 = 날짐승 - 들짐승 # 위와는 반대로 날짐승에서 들짐승에 포함된 걸 뺀 집합
print(날짐승_차_들짐승)

'''
코드 5-72 두 집합의 대칭차 구하기

>>> 들짐승.symmetric_difference(날짐승)  # 들짐승과 날짐승의 대칭차
{'사자', '늑대', '곰', '독수리', '매'}
'''

들짐승_대칭차_날짐승 = 들짐승.symmetric_difference(날짐승)
날짐승_대칭차_들짐승 = 들짐승 ^ 날짐승
print(들짐승_대칭차_날짐승)
print(날짐승_대칭차_들짐승)

'''
코드 5-74 부분집합 검사하기

>>> 들짐승.issubset(짐승)    # 들짐승이 짐승의 부분집합인가?
True

>>> 들짐승.issubset(날짐승)  # 들짐승이 날짐승의 부분집합인가?
False

>>> 들짐승 <= 짐승
True

>>> 들짐승 <= 날짐승
False
'''


들짐승_subsetof_짐승_check = 들짐승.issubset(짐승)
들짐승_subsetof_날짐승_check = 들짐승.issubset(날짐승)

# print(들짐승_subsetof_짐승_check)
# print(들짐승_subsetof_날짐승_check)


'''
그림 5-12 A와 B는 서로소 집합

서로소 집합을 검사하려면 isdisjoint(다른집합) 메서드를 사용한다.

코드 5-76 서로소 집합 검사하기

>>> 들짐승.isdisjoint(날짐승)
False

>>> 들짐승.isdisjoint(바다생물)
True
'''


'''
집합은 수정 가능한 데이터다. 이미 정의한 집합에 원소를 추가하거나 삭제할 수 있다. 다음과 같은 메서드를 사용한다.

add(데이터): 데이터를 원소로 추가
discard(원소): 원소 제거
remove(원소): 원소 제거 (원소가 없으면 오류)
pop(): 아무 원소나 꺼낸다 (집합이 비어있으면 오류)

'''
'''
들짐승.add('인간')      # 들짐승에 인간 추가
들짐승
{'사자', '늑대', '곰', '인간', '박쥐'}

들짐승.discard('인간')  # 인간 제거
들짐승
{'사자', '늑대', '곰', '박쥐'}

들짐승.remove('곰')     # 곰 제거
들짐승
{'사자', '늑대', '박쥐'}

들짐승.pop()            # 아무 원소나 꺼내기
'사자'

들짐승
{'늑대', '박쥐'}

들짐승.clear()          # 모든 원소 제거
들짐승
set()
'''

'''연습문제 5-15 일하는 날

is_working_day() 함수를 정의하라. 이 함수는 요일을 입력받아 그 요일이 여러분이 쉬는 날이면 True, 아니면 False를 반환한다.
'''

def is_working_day(day):
    day_set = {day}
    working_day = {
        '월요일', '화요일', '수요일', '목요일', '금요일'
    }
    return day_set.issubset(working_day)

print(is_working_day('화요일'))

'''
연습문제 5-16 집합 계산 1

0 이상 1000 미만의, 3과 4의 공배수는 모두 몇 개인지 계산하라.

연습문제 5-17 집합 계산 2

0 이상 1000 미만의, 3의 배수이되 4의 배수는 아닌 수는 모두 몇 개인지 구하라.
'''

print(len(set(list(range(0,1000,3))+list(range(0,1000,4))))-1)
# 3과 4의 합집합으로 구해도 되고 이처럼 리스트를 합치고 그냥 set 처리 해도 중복 제거 되어서 괜춘 0이 포함되어 있으니 빼주자

print(len(set(list(range(0,1000,3)))-set(list(range(0,1000,4))))-1)

'''
5.4.5 프로즌셋
집합은 리스트, 사전처럼 수정이 가능한 데이터다. 한 번 집합을 정의한 뒤에도 원소를 추가, 삭제할 수 있다.

수정이 불가능한 집합 컬렉션을 정의하고 싶다면 프로즌셋(frozenset)을 사용하면 된다. 프로즌셋을 정의하는 방법은 다음과 같다.

공집합 프로즌셋: frozenset()
집합에서 정의하기: frozenset({원소 1, 원소 2, 원소 3, ...})
시퀀스에서 정의하기: frozenset([원소 1, 원소 2, 원소 3, ...])
프로즌셋은 집합과 사용 방법이 거의 동일하고 연산과 메서드도 공유한다. 단
, 내용을 수정하는 연산과 메서드는 지원하지 않는다. 
프로즌셋이 필요한 경우는 거의 모두 집합으로 대체 가능하여 자주 사용되지는 않는다. 이런 것이 있다는 것만 알아 두자.
'''


