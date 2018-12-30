#선택

'''
선택은 프로그래밍에서도 매우 중요한 요소다.
앞 장까지 만들어 본 프로그램은 언제나 한 가지 흐름으로만 실행되었는데,
선택지와 조건을 고려하지 않았기 때문이다.
프로그램에 선택지와 조건을 마련해 두면 컴퓨터가 상황에 따라 적절하게 작업을 수행하도록 할 수 있다.
'''

#6.1.2 if 문


'''
코드 6-2 일요일 낮에 할 일 선택 1 (if1.py)
'''

# print('일요일 낮의 날씨를 입력해주세요:')
# 날씨 = input()  # ❶
#
# if 날씨 == '비':  # ❷
#     print('집에서 프로그램을 만들자.')
#
# if 날씨 != '비':  # ❸
#     print('공원에서 스케이트보드를 타자.')

'''
실행 결과:

일요일 낮의 날씨를 입력해주세요:
맑음
공원에서 스케이트보드를 타자.
실행 과정을 생각해 보자. ❶에서 사용자의 입력에 의해 
날씨 변수에 '맑음'이 대입되었다. 
따라서 ❷의 if 문에서는 조건이 '맑음' == '비'가 되므로 거짓으로 평가되어 본문이 실행되지 않는다. 
❸의 if 문에서는 조건이 '맑음' != '비'가 되므로 참으로 평가되어 본문이 실행된다. 
그 결과, 화면에 ‘공원에서 스케이트보드를 타자.’라는 텍스트만 출력되었다.

개념 정리

if 문을 이용해 조건에 따라 실행할 코드를 선택하도록 할 수 있다.

선택은 여러 가능성이 열려 있어야 의미가 있다
선택은 여러 가능성이 열려 있어야 의미가 있다. 조건이 언제나 똑같이 평가되거나, 
선택지가 하나 뿐이라면 선택을 할 필요가 없다. 다음 경우를 생각해보자.

조건이 항상 참일 때: if 문의 본문이 항상 실행된다. if 문 없이 코드 본문을 작성하면 된다.
조건이 항상 거짓일 때: if 문의 본문이 절대 실행되지 않는다. 코드를 작성할 필요가 없다.
선택지가 하나뿐일 때: 조건을 따지지 않고 실행해야 할 코드다. if 문 없이 코드 본문을 작성하면 된다.
초보 프로그래머는 항상 참인 조건 또는 항상 거짓인 조건을 작성하는 실수를 저지를 때가 있다. 예를 들어, 
10 < x and x < 5 같은 조건은 변수 x에 어떤 값이 대입되든지 항상 거짓이 되는 조건이다.
수직선과 진리표(가능한 모든 조건과 결과를 나열한 표) 등을 이용하면 틀린 조건을 작성하는 것을 예방할 수 있다.

개념 정리
if 문을 이용해 조건에 따라 실행할 코드를 선택하도록 할 수 있다.
'''

#6.1.3 함수 안에서 if 문 활용하기
'''
abs() 함수는 입력받은 수의 절대값을 반환한다. if 문을 사용해 이 함수와 같은 함수를 직접 정의할 수 있다.

먼저, 어떤 수 N의 절대값을 구하는 방법을 생각해 보자.

N이 0 이상이면 절대값은 N이다.
N이 0 미만이면 절대값은 -N이다.
이 계산법에서는 ‘N이 0 이상이다’라는 조건과 
'N이 0 미만이다’라는 조건에 따라 절대값을 구하는 방법이 다르다. 
이를 코드로 옮긴다면, 조건에 따라 실행할 코드가 달라야 하므로 if 문을 사용해야 한다. 함수로 작성해 보자.
'''

# def 절대값(n) :
#     """숫자 n을 입력받아 양수이며 절대값 n을 출력 음수이면 절대값 -n을 출력하는 함수"""
#     if n >= 0 :
#         return n # n이 0 이상이면 n을 반환한다
#     if n < 0 :
#         return -n # n이 0 미만이면 -n을 반환한다
#
# print('10의 절대값:', 절대값(10))
# print('-5의 절대값:', 절대값(-5))
#
# print(abs(0))

#6.1.4 else: 그렇지 않다면

'''
if 조건:
    본문 1   # 조건이 참일 때 실행할 코드
    
else:
    본문 2   # 조건이 거짓일 때 실행할 코드
'''
#코드 6-4 일요일에 낮에 할 일 선택
# print('일요일 낮의 날씨를 입력해주세요:')
# 날씨 = input()
#
# if 날씨 == '비':
#     print('집에서 프로그램을 만들자.')
# else:  # ❶ 날씨 == '비'가 아닌 경우
#     print('공원에서 스케이트보드를 타자.')


# 이런 내용들은 서로 모순인 조건에 대해서만 사용할 수 있다 A가 아니라면 B인 상황에서만 사용가능
# 집합에서 A + B = U / A - B = A 인 상황이 되어야 한다

'''
pass 문: 코드 실행 생략하기
파이썬에는 컴퓨터에게 아무 것도 하지 말고 다음 코드로 넘어가도록 지시하는 명령,
pass 문이 있다. pass 문을 이용하면 if 문에서 조건이 참일 때 아무 것도 하지 않도록 지시할 수 있다.
'''

#코드 6-5 코드 실행 생략하기

# if 날씨 == '비':
#     pass  # 조건이 참이어도 아무 것도 실행하지 않는다

'''
개념 정리

else 절을 이용해 if 문의 조건이 거짓일 때 실행할 코드를 지정할 수 있다.
서로 모순인 조건의 두 선택지를 if … else … 구문으로 나타낼 수 있다.
코드 블록을 비워둘 때 pass 문을 사용한다.
'''

#6.1.5 elif: 선택지가 여러 개일 때

#코드 6-8 일요일 낮에 할 일 선택 3 (if3.py)
# print('일요일 낮의 기온을 입력해주세요:')
# 기온 = float(input())
#
# if 28.0 <= 기온: # 1. 첫 번째 선택지
#     print('바닷가에서 더위를 피하자')
#
# elif 16.0 <= 기온: # 위 조건이 거짓일 때 검사
#     print('공원에서 스케이트보드를 타자.')
#
# elif 8.0 <= 기온 : # 위 2 조건이 거짓일 때 검사
#     print('도서관에서 책을 읽자.')
#
# else: # 모든 조건이 거짓일 때 검사
#     print ('집에서 프로그램을 만들자. ')


'''
코드 6-9 elif 를 사용하지 않고 if 문으로만 선택지를 나타냈을 때 (if4.py)

print('일요일 낮의 기온을 입력해주세요:')
기온 = float(input())  # 입력받은 기온을 실수로 변환하자

if 28.0 <= 기온:
    print('바닷가에서 더위를 피하자.')

if 16.0 <= 기온:  # ❶ 
    print('공원에서 스케이트보드를 타자.')

if 8.0 <= 기온:   # ❷
    print('도서관에서 책을 읽자.')
else:
    print('집에서 프로그램을 만들자.')
실행 결과:

일요일 낮의 기온을 입력해주세요:
17.0
공원에서 스케이트보드를 타자.
도서관에서 책을 읽자.
위 코드를 실행하면 기온이 17.0일 때 ‘공원에서 스케이트보드를 타자.’와 ‘도서관에서 책을 읽자.’가 함께 출력된다. 기온이 17.0이면 ❶의 조건도 만족하고 ❷의 조건도 만족하기 때문이다. 원래는 한 가지 선택지만 출력하려는 프로그램이므로 잘못 작성된 프로그램이다.

elif 절과 else 절을 이용하면 여러 선택지를 묶어 그 중에서 한 번만 선택하도록 한다. 반대로 각 선택지를 별도의 if 문으로 작성하면 작성한 if 문의 개수만큼 선택이 일어난다. 이 차이를 잘 알아두도록 하자.
'''
'''
개념 정리

여러 개의 선택지 중에서 하나를 선택하여 실행해야 할 때, if … elif … else … 구문을 이용한다.

'''


#6.1.6 여러 조건 결합하기

'''
6.1.6 여러 조건 결합하기
if 문에서 여러 조건을 결합하고 싶을 때가 있다. 예를 들어, 
날씨만 보는 것이 아니라 오늘이 무슨 요일인지도 확인해야 할 일을 올바르게 결정할 수 있다. 
4.4절에서 배운 and 연산과 or 연산을 사용하면 여러 조건을 결합할 수 있다.
'''

#and: 여러 조건이 모두 참이다

#코드 6-10 여러 조건이 모두 참일 때 (and 연산)
# print('날씨를 입력해주세요: ')
# 날씨 = '맑음'
# print('요일을 입력주세요: ')
# 요일 = '토요일'
#
#
# if (날씨 == '맑음') and (요일 == '일요일'):
#     print('공원에서 스케이트보드를 타자.')
#
#
# if 요일 == '토요일':
#     print('여유로운 시간을 보내자.')
# else:
#     if 요일 == '일요일':
#         print('여유로운 시간을 보내자.')


'''
조건을 결합할 때 주의할 점
or 연산을 이용해 조건을 결합할 때 초보 프로그래머가 저지르기 쉬운 실수가 있다. 
‘계절이 봄 또는 가을이다’ 라는 조건을 나타낼 때, 다음 중 어느 것이 올바른 표현인지 생각해 보자.

계절 == '봄' or '가을'
계절 == '봄' or 계절 == '가을'
1은 틀렸고 2가 올바르다. 1은 비교식 계절 == '봄'과 문자열 '가을'을 or 연산한 것이다. 
문자열 '가을'은 항상 참으로 평가되므로 1은 계절 변수의 값이 무엇이든, 언제나 참으로 평가된다.

일상어에서는 반복되는 단어를 생략할 때가 많다. ‘계절이 봄 또는 가을이다’라고 할 때, 
'가을이다’는 ‘계절이 가을이다’를 줄인 것이다. 이 표현을 프로그래밍 코드로 옮길 때는 
'계절이 봄이다 또는 계절이 가을이다’와 같이 완전한 문장으로 표현해야 하며, 따라서 2가 올바르다.
(계절 == '봄') or (계절 == '가을')과 같이 or 양변의 비교식을 괄호로 둘러싸 표현하면 실수를 줄일 수 있다.
'''

'''
개념 정리

and 연산과 or 연산을 이용해 여러 개의 조건을 하나로 합칠 수 있다.
논리 연산을 잘못 작성하지 않도록 주의해야 한다.
'''
# 6.1.7
''' 카페에서 월요일에만 카페 라테를 1,000 원에 판매하기로 했다. 
월요일에만 음료 가격을 다르게 하려면 어떻게 하면 좋을까?

조건부 식(conditional expression)은 조건에 따라 값을 구하는 식이다. 
덧셈식이 좌변과 우변의 값에 따라 값을 구하는 것처럼, 조건부 식은 조건을 판단한 결과에 따라 값을 구한다. 
조건부 식은 형태가 if 문과 비슷하며, 다음과 같은 양식으로 작성한다.

참값 if 조건 else 거짓값
'''

# 코드 6-14 요일에 따라 음료 가격 구하기 (조건부 식)

# 가격 = 1000 if 요일 == '월요일' else 2500


# 코드 6-15 요일에 따라 음료 가격 구하기 (if 문)
#
# if 요일 == '월요일':
#     가격 = 1000  # ❶ if 문의 본문에 대입문이 하나 필요하고...
# else:
#     가격 = 2500  # ❷ else 절의 본문에도 대입문이 하나 필요하다가격 = 1000 if 요일 == '월요일' else 2500

'''
연습문제
연습문제 6-1 할인된 가격 계산

어떤 상점에서는 상품을 한꺼번에 많이 구매하면 다음과 같이 상품 가격을 할인해 준다.

10개 미만: 상품 하나에 100원
10개 이상 30개 미만: 상품 하나에 95원
30개 이상 100개 미만: 상품 하나에 90원
100개 이상: 상품 하나에 85원
이 쇼핑몰에서 구매할 상품 개수를 입력받아, 총 지불해야 할 가격을 계산하는 함수 price()를 정의하라.

함수를 정의한 후에는 이 함수에 여러 상품 개수를 입력하여 결과가 올바른지 확인해 보아라.
'''

# def price(count=10):
#     """상점에서 갯수를 입력 받아 그 상품들의 가격을 계산하는 함수, 갯수에 따라서 가격이 달라진다"""
#     if count >= 0 and count < 10 and type(count) == int:
#         price = 100 # 10개 이하면 100원
#         return count * price
#     elif count >= 10 and count < 30 and type(count) == int :
#         price = 95 # 10개 이상 30개 미만이면 95원
#         return count * price
#     elif count >= 30 and count < 100 and type(count) == int :
#         price = 90 # 30개 이상 100개 미만이면 90원
#         return count * price
#     elif count >= 100 and type(count) == int:
#         price = 85 #100개 이상 85원
#         return count * price
#     else:
#         return "0이상인 정수만 입력가능합니다. count를 다시 입력해주세요"
#
# print(price(3153.5)) # int만 받아서 처리하게 하고 나머지는 에러가 나게 하려면 어떻게 해야 할까
# #type(int) 검사를 추가해서 int를 받은 게 아니라면 계산하지 않게 한다 물건을 0.1개 단위로 팔 수는 없으니
#


'''
연습문제 6-2 윤년 계산

연을 매개변수로 입력받아 그 해가 윤년인지 아닌지를 True 또는 False로 반환하는 함수 
is_leap_year()를 정의하라.

윤년이란 1년이 365일이 아니라 366일로 이뤄진 해다. 
윤년에는 2월이 28일까지가 아니라 29일까지 있다. 어떤 해가 윤년인지 아닌지를 판단하는 규칙은 다음과 같다.

그 해의 수가 4로 나누어 떨어지면 윤년이다. (예: 1996년은 윤년이다)
단, 그 해의 수가 100로 나누어 떨어지면 윤년이 아니다. (예: 1900년은 윤년이 아니다.)
단, 그 해의 수가 400으로 나누어 떨어지면 윤년이다. (예: 2000년은 윤년이다.)
'''

def is_leap_year(year = 2000):
    if year % 400 == 0 or year % 4 == 0 and year %100 != 0 :
        return True
    else:
        return False
print(is_leap_year(2000))

# 부분집합이라 볼 때 가장 작은 if 부터 먼저 나오도록 하고 가장 범위가 큰 대상을 나중에 나오게 해야 모든 값을
# if로 표현하는 것이 가능해진다

'''
연습문제 6-3 한 달의 길이

연과 월을 매개변수로 입력받아, 그 달이 며칠까지 있는지 반환하는
함수 days_in_month()를 작성하라. 이 때, 2월의 길이는 윤년인지 아닌지에 따라 다르다. 
윤년 계산을 위해 연습문제 6-2에서 만든 함수를 활용하라.
'''

def days_in_month(year,month):
    if is_leap_year(year) and month == 2:
        return 29
    elif is_leap_year(year) == False and month == 2:
        return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30

print(days_in_month(2000,2))
# 좀더 쉽게 하는 방법이 없을까 ?


'''
연습문제 6-4 비만도 검사

사용자로부터 키와 몸무게를 입력받아 비만 정도를 알려주는 프로그램을 작성하라.

비만도를 측정하는 방법:

체질량 지수를 구한다. 키가 t 미터, 체중이 w 킬로그램일 때, 체질량 지수는 w / (t * t) 다.
1예서 구한 체질량 지수가 18.5 미만이면 저체중, 
18.5 이상 23 미만이면 정상, 23 이상 25 미만이면 과체중, 25 이상이면 비만이다.


실행 예:
키를 입력하세요(m): 1.75
몸무게를 입력하세요(kg): 65
정상입니다.
힌트: 문제를 필요한 만큼 여러 단계로 나누어, 여러 개의 함수를 정의하여 해결하자.
'''
def 체질량지수(t=1.75,w=50):
    '''키(m) 값 : t와 몸무게(kg) 값 :w 를 입력받아 체질량 지수를 계산하는 함수 '''
    return w / (t*t)

def 체질량_체크(체질량지수 = 20):
    """체질량 지수를 바탕으로 비만도를 체크하는 핫무 """
    체질량지수 = round(체질량지수,2)
    if 체질량지수 >=  25:
        return "당신의 체질량 지수는" + str(round(체질량지수,2)) + "이며 비만입니다. 다이어트를 하세요."
    elif 체질량지수 >= 23 and 체질량지수 < 25 :
        return "당신의 체질량 지수는" + str(round(체질량지수,2)) + "이며 과체중입니다. 주의하세요."
    elif 체질량지수 >= 18.5 and 체질량지수 <23 :
        return "당신의 체질량 지수는" + str(round(체질량지수,2)) + "이며 정상입니다. 축하드려요!"
    elif 체질량지수 < 18.5:
        return "당신의 체질량 지수는" + str(round(체질량지수,2)) + "이며 저체중입니다. 살을 찌우세요!"

# print('키를 입력하세요(m):',end='')
# t = round(float(input()),2)
# print('몸무게를 입력하세요(kg):',end='')
# w = round(float(input()),2)
# print(체질량_체크(체질량지수(t,w)))

def absolute_number(a=0):
    """정수를 입력받아 절대값을 출력하는 함수 , 조건식으로 작성"""
    a = int(a)
    a = a if a >= 0 else -a
    return a

print(absolute_number(5))

'''
요점 정리

컬렉션을 순회하며 컬렉션의 각 요소를 읽고 사용할 수 있다.
for 문을 이용하면 컬렉션을 간편하게 순회할 수 있다.
'''