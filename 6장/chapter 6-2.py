#6.2 반복

'''
반복이란 같은 작업을 여러 번 실행하는 것이다. 매일 아침 7시에 전화벨 울리기,
영화표 구매가 가능한지 5분마다 확인하기, 숫자를 세다가 3, 6, 9가 나오면 박수 치기…

반복 작업을 프로그래밍하는 방법
숫자를 1부터 4까지 차례대로 화면에 출력하는 프로그램을 작성해 보자.
'''


#코드 6-16 1부터 4까지 출력하는 프로그램 1

print(1)
print(2)
print(3)
print(4)


'''
두 번째 문제는 이 프로그램이 ‘작업의 반복’이 아니라 ‘작업들’을 지시한다는 점이다. 
“네 번 하시오.”가 아니라 “하시오. 하시오. 하시오. 하시오.”라고 지시하는 것이다. 
반복할 횟수가 많아질수록 프로그래머가 작성해야 할 ‘하시오’ 코드도 많아질 것이다. 
게다가 몇 번이나 반복해야 할지 미리 알 수 없는 경우에는 이 방법을 아예 쓸 수 없다.

이 문제를 하나씩 해결하며, 반복 작업을 우아하게 지시하는 방법을 알아 보자.
'''

#6.2.2 반복의 한 주기를 온전히 나타내기


#코드 6-17 코드 6-16의 한 주기

print(1)

# 코드 6-18 온전히 표현한 한 단계의 작업

number = 0
number += 1     # 수를 1 증가시킨다
print(number)   # 수를 출력한다


#코드 6-19 1부터 4까지 출력하는 프로그램 2

number = 0      # 수를 세기 위해 변수가 필요하다

number += 1     # 수를 1 증가시킨다
print(number)   # 수를 출력한다
number += 1
print(number)
number += 1
print(number)
number += 1
print(number)

#개념 정리
#반복 코드를 작성할 때는 반복의 한 주기를 온전히 파악하고 작성하는 것이 중요하다.

#6.2.3 while 문: 조건이 유지되는 동안 반복하기


'''
while 문은 지정한 조건이 유지되는 동안 코드를 계속 반복하는 명령이다.
 while 문은 기능이 단순해서 사용하기 다소 불편할 때도 있지만,
특별한 제약 없이 다양한 반복 처리를 수행할 수 있다. while 문을 작성하는 양식은 다음과 같다.

while 조건:   # ❶ 첫 행
    본문      # ❷ 조건이 참인 동안 반복 실행할 코드 블록

영어 단어 ‘while’은 “… 인 동안”이라는 뜻이고, while 문을 우리 말로 옮기면 
“조건이 유지되는 동안 본문의 코드를 반복 실행하라”라는 뜻으로 풀이할 수 있다.
'''

i = 0

while i < 3: # 유지할 조건을 골라준다
    print('안녕') # 반복할 반복 코드를 입력해준다
    i += 1 # i에 1을 더한다 식에다 +를 써줘야한다


'''
코드를 N번 반복하는 while 문 패턴

반복을 시작하기 전, 반복 횟수를 기억할 변수(i)에 0을 대입한다.
while 문의 반복 유지 조건을 i < N으로 지정한다.
while 문의 본문 코드 블록 안에서 필요에 따라 i의 값을 활용한다.
while 문의 본문 코드 블록 안에서 i의 값을 1 증가시킨다.

'''

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
index = 0

while index < len(rainbow):
    print(rainbow[index])
    index += 1

#흐름이 예정되지 않은 반복 -> 사용자가 직접 반복 흐름을 통제하는 프로그래밍
# text = "아무 메시지나 입력하세요. 그만하려면 '그만'을 입력하세요."
# while text != '그만':
#     print('컴퓨터:' + text)
#     text = input()


'''
while True: 
로 활용하면 무한히 반복되는 반복문을 활용할 수 있다 
무한 반복이 활용되는 곳은 많다. 몇 가지만 예를 들어 보자.

사용자와 계속 상호작용하는 프로그램
웹 문서를 지속적으로 탐색하며 정보를 수집하는 크롤링 프로그램
음악을 무한 반복 재생하는 프로그램
컴퓨터가 켜진 동안 내내 시스템을 관리하는 운영 체제
그런데 이런 프로그램들도 언젠가는 무한 반복을 중지해야 할 때가 있을 것이다. 
사용자가 프로그램 종료 버튼을 눌렀거나, 더이상 탐색할 문서가 없을 수도 있다. 
언젠가는 이런 예외 상황이 발생할 것이고 그 때는 반복을 중지해야 한다.
반복을 임의로 중지하는 방법은 6.2.5에서 설명한다.

요점 정리

while 문의 조건으로 True를 지정하여 무한 반복을 지시할 수 있다.

while 문을 이용하면 모든 반복 상황을 프로그래밍할 수 있다. 
흐름이 예정되지 않은 반복이나 무한 반복을 나타낼 때 특히 유용하다. 
하지만 작업을 순차적으로 처리하거나 컬렉션을 순회할 때는 for 문을 사용하는 것이 더 편리하다.
'''

'''
6.2.4 for 문: 컬렉션 순회하기
for 문은 while 문과 마찬가지로 코드를 반복 실행하는 명령이다
. while 문이 여러 목적에 활용할 수 있는 범용적인 반복 기능이라면, 
for 문은 순차적 처리와 컬렉션 순회에 특화된 반복 기능이다. 
for 문을 이용하면 반복 횟수를 관리하는 데 신경을 쓰지 않고 간단히 컬렉션을 순회할 수 있다.

for 문을 작성하는 양식을 살펴보자.

for 변수 in 컬렉션:   # ❶ 첫 행
    본문              # ❷ 컬렉션의 각 항목마다 반복 실행할 코드 블록
'''




#코드 6-24 무지개 색 리스트의 내용을 순회하며 출력 (for1.py)

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for color in rainbow:
    print(color)


'''
코드 6-24의 실행 결과는 코드 6-21과 동일하다. 
이처럼 컬렉션을 순회할 때 while 문 대신 for 문을 사용하면 반복 횟수를 직접 관리하지 않아도 되고, 
코드를 더 간결하게 작성할 수 있다.

한 가지 예를 더 들어보자. 다음은 시퀀스에 들어 있는 모든 수의 합계를 계산하는 
함수(sum() 함수를 흉내낸 것)를 for 문을 이용해 정의한 것이다.
'''

#코드 6-25 시퀀스의 모든 수의 합을 계산하는 함수 (my_sum.py)
def my_sum(numbers):
    """numbers의 모든 요소의 합을 나타낸다"""
    total = 0
    for n in numbers:
        total += n
    return total

print (my_sum([1,2,3,4,5]))

# 코드 6-26 1부터 10까지의 모든 짝수의 합 (for2.py)

total = 0  # 합계

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if n % 2 == 0:  # n 이 짝수인 경우,
        total += n  # total에 n을 더함

print(total)


total = 0  # 합계

# for n in range(2, 10000001, 2):  # 2부터 1천만까지 2씩 증가하는 레인지를 순회
#     total += n                   # n이 짝수인지 검사하지 않고 total에 더해도 된다
#
# print(total)

# 요점 정리

# for 문과 레인지를 이용해 등차수열을 순회할 수 있다.

# print('안녕을 몇 번 반복하시겠습니까?')
# n = int(input())    # 반복할 횟수
#
# for _ in range(n):  # 코드를 n번 반복 실행
#     print('안녕')

'''요점 정리

for 문과 레인지를 이용해 코드를 N회 반복 실행할 수 있다.'''

# for 문과 while 문의 구분은 반복문이

#continue 문: 이번 주기의 실행을 중지
#continue 문은 반복 도중에 ‘한 주기의 실행’을 중지하고 다음 주기로 넘어도록 하는 명령이다. continue 문을 사용하려면 for 문 또는 while 문의 본문 안에서 continue를 입력하면 된다. 다음은 for 문에서 continue 문을 사용한 예다.

#코드 6-31 continue 문

for i in range(4):
    print('현재 반복 주기:', i)      # ❶
    continue                         # 현재 반복 주기를 중지하고 다음 주기로 넘어간다
    print('다음 반복 주기:', i + 1)  # ❷

#break 문: 반복 전체를 중지
#break 문은 반복의 한 주기만이 아니라 ‘반복 전체’를 중지시킨다. 사용법은 continue 문과 동일하다. 다음은 for 문에서 break 문을 사용한 예다.

#코드 6-32 break 문

for i in range(4):
    print('현재 반복 주기:', i)      # ❶
    break                            # 반복 전체를 중지한다
    print('다음 반복 주기:', i + 1)  # ❷

total  = 0

# 코드 6-33 continue 문과 break 문의 활용

total = 0
#
# while True:
#     print('더할 수를 입력하세요: ', end = '')
#     user_input = input()

# 코드 6 - 33 continue 문과 break 문의 활용

total = 0

'''
while True:  # ❶ 본문 코드를 무한 반복한다
    print('더할 수를 입력하세요: ', end='')
    user_input = input()

    if user_input == '그만':  # ❷ '그만'이 입력되면 반복을 종료한다
        break

    if not user_input.isnumeric():  # ❸ 입력이 수가 아니면 다음 주기로 넘어간다
        print('잘못된 입력입니다.')
        continue

    total += int(user_input)
    print('합계:', total)

print('프로그램을 종료합니다.')
'''

#코드 6-35 else 절이 실행되지 않는 경우

i = 0
while(i < 100):
    print(i, '번째 실행')
    i += 1
    if (i > 2):
        print('반복 중지')
        break
else:
    print('반복 완료')

'''
for 변수 in 컬렉션:
    본문 1            # 컬렉션의 각 항목마다 반복 실행할 코드 블록
else:
    본문 2            # 반복이 정상 종료된 직후 실행할 코드 블록
    
    요점 정리

while 문에서 else 절의 본문은 반복이 정상적으로 종료되었을 때 실행된다.
for 문에서 else 절의 본문은 순회가 정상적으로 종료되었을 떄 실행된다.
반복 도중 break 문이 실행되면 else 절의 본문이 실행되지 않는다.
'''


def 첫_짝수_찾기(numbers):
    """numbers에서 첫 번재 짝수를 찾아 화면에 출력한다."""
    for n in numbers:
        if n % 2 == 0 :
            print(n, '이 첫 짝수입니다.')
            break;
    else:
        print('짝수가 없습니다. ')

첫_짝수_찾기([1,3,5,66,33])
첫_짝수_찾기([3,45,51,1])

for i in range(2,10):
    for j in range(1,10):
        print(i * j, end = '   ')
    print()

# 요점 정리
#반복 코드 속에 반복 코드를 작성하여 중첩할 수 있다.



'''
연습문제 6-6 5의 배수의 합계 (while 문을 사용하여)

1백 이상, 1만 미만인 자연수 가운데 5의 배수를 모두 합하면 얼마인지 while 문을 사용해 계산해 보아라.

힌트: 초기값이 1백이고 각 반복 주기마다 5씩 증가하는 변수를 사용해 보자.
'''
i = 100
j = 0
while i >= 100 and i < 10000 :
    j += i
    i += 5
    print(i)
    print(j)

# iiiii = sum(list(range(100,10000,5)))
#
# print(iiiii)


'''
연습문제 6-7 5의 배수의 합계 (for 문을 사용하여)

연습문제 6-6의 문제를 for 문과 레인지를 사용해 계산해 보아라.

'''
suma = 0
for i in range(100,10000,5):
    suma += i

print(suma)


j = 0
for i in range(100,10000,5):
    j += i
    i += 5
    print(i)
    print(j)


def max_for(numbers = [1,2,3,4,5]):
    """리스트를 전달받아 리스트에서 가장 큰 요소를 반환한다."""
    candidate = numbers[0]
    for i in numbers:
        if i > candidate:
            candidate = i
    return candidate
print(max_for())


def find(needle,haystack) :
    """"needle을 입력 받아 haystack(리스트)에서 몇 번째 원소인지 출력하는 함수
    없으면 None을 출력한다"""
    for e in haystack
        if needle = e
            return e
    else:
        return None



def find_testor(function):
    print(function(5, [1, 2, 3, 4, 5]) == 4)
    print(function(3, [4, 3, 5, 1, 2]) == 1)
    print(function(9, [1, 2, 3, 4, 5]) is None)


def find(needle, haystack):
    for i in range(len(haystack)):
        if needle == haystack[i]:
            return i
        else:
            continue

def index(needle, haystack):
    index_num = 0
    for element in haystack:
        if element == needle:
            return index_num
        index_num = index_num + 1
    return None


def yeono_find(needle, haystack):
    i = 0
    for element in haystack:
        if element == needle:
            return i
        i += 1

def solve(n):
    if len(str(n)) < 2:
        return n
    else:
        next_number = int(str(n)[0]) * int(str(n)[1])
        return solve(next_number)
