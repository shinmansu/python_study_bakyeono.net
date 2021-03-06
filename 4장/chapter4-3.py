#텍스트


#아스키코드와 유니 코드
'''
표준안 중에서 아스키 코드(ASCII code, 미국정보교환표준부호)와 유니코드(Unicode)가 가장 널리 사용되고 있다.

아스키 코드는 문자 하나를 비트 일곱 개로 표현한다. 7 비트로 표현할 수 있는 경우의 수는 128가지다.
그래서 아스키 코드에는 숫자, 알파벳 대소문자, 기호 등을 포함해 128가지 문자만이 할당되어 있다.
아스키 코드는 간단해서 다루기 쉽고 대부분의 컴퓨터에서 사용할 수 있을만큼 보편적이다.
하지만 알파벳이 아닌 문자는 표현할 수 없다는 한계가 있다.

알파벳 외의 문자를 사용하는 나라들은 저마다 문자 코드 체계를 만들어 사용했다. 하지만 정보는 국제적으로 교환할 필요가 있다.
-> 파이썬은 유니코드로 부호화를 한다
'''

#문자열
'''
파이썬은 텍스트 데이터를 취급하기 위한 문자열(string, 줄여서 str)이라는 데이터 유형을 제공
'' 혹은 ""로 감싸는 텍스트 데이터를 문자열이라 한다. 

문자열은 문자를 나열한 것

프로그래밍 언어 중에는 개별 문자와 문자열을 서로 다른 유형으로 구분하는 것도 있다. 
파이썬에서는 개별 문자든 문자열이든 모두 문자열로 취급한다.
(‘문자 하나’는 문자가 하나만 나열된 ‘문자열’이다.) 
이렇게 문자와 문자열을 동일한 유형으로 취급하면 텍스트 데이터의 취급 방법이 통일되어 편하다.
'''

print("today's coffee")
# print('today's coffee') # 에러가 난다
print('today\'s coffee') # 작은따옴표를 이스케이프 해주면 명령을 처리하지 않기 때문에 정상적으로 출력된다

'''
이스케이프로 특별한 문자 입력하기
이스케이프란 일반적인 방법으로 입력하기 어려운 특별한 문자를 입력하는 방법이다. 
이스케이프를 하려면 먼저 이스케이프 기호 백슬래시(\)를 쓰고 바로 붙여서 이스케이프할 문자를 적는다. 
이스케이프를 통해 표현해야 하는 특별한 문자로는 다음과 같은 것이 있다.

\\: 백슬래시
\': 작은따옴표 (작은따옴표 안에서)
\": 큰따옴표 (큰따옴표 안에서)
\n: 개행 문자 (라인 피드. 다음 행으로 바꿈)
\r: 개행 문자 (캐리지 리턴. 커서를 행의 앞으로 이동. 잘 사용하지 않는다.)
\t: 탭 문자
'''

text = 'Today\'s coffee:\n"카페 라테"\n"아메리카노"'
print(text)

'''
라인 피드와 캐리지 리턴

개행 문자는 왜 두 개(\n과 \r)일까? 개행 문자는 과거 인쇄기를 제어하는 방식과 연관이 있다. 
\n은 라인 피드(line feed)라는 기호로, 인쇄기에게 종이를 한 행만큼 올리라고 지시한다. 
\r은 캐리지 리턴(carriage return)이라는 기호로, 인쇄기의 활자를 찍는 팔을 원위치로 옮기라고 지시한다. 
옛날 컴퓨터는 데이터 출력을 인쇄기로 했는데, 문자 출력 위치를 다음 행으로 바꾸려면 
\r\n을 둘 다 수행해야 했기 때문에 두 문자가 모두 필요했다. 
오늘날에는 인쇄기를 제어하는 방식은 달라졌다. 
하지만 라인 피드와 캐리지 리턴을 이용해 텍스트 데이터에서 개행을 나타내는 방식은 그대로 남았다.

그런데 운영 체제마다 개행을 나타내는 방식에 차이가 있다. 
윈도우 계열의 OS에서는 개행을 \r\n으로 나타내고, 
유닉스 계열의 OS(리눅스, 맥OS 등)에서는 개행을 \n만으로 나타낸다. 
그래서 리눅스에서 작성한 텍스트 
파일을 윈도우의 메모장으로 열면 개행 문자가 깨져 보일 수 있다.

파이썬 문자열에서는 \n 만으로 개행을 표현한다. \r을 사용하는 경우는 거의 없다.
'''

# print(r'다음 행으로 넘어갈 때는 개행 문자(\n)을 쓰세요.')
#
poem = '죽는 날까지 하늘을 우러러\n한 점 부끄럼이 없기를,\n잎새에 이는 바람에도\n나는 괴로워했다.\n별을 노래하는 마음으로\n모든 죽어 가는 것을 사랑해야지\n그리고 나한테 주어진 길을\n걸어가야겠다.\n오늘밤에도 별에 바람이 스치운다.'
# print(poem)
#
# poem1 = """죽는 날까지 하늘을 우러러
# 한 점 부끄럼이 없기를,
# 잎새에 이는 바람에도
# 나는 괴로워했다.
# 별을 노래하는 마음으로
# 모든 죽어 가는 것을 사랑해야지
# 그리고 나한테 주어진 길을
# 걸어가야겠다.
# 오늘밤에도 별에 바람이 스치운다.
# """

# print(poem1)

print(len('아메리카노'))

text = '카페 라테'

print(text[0])
print(text[1])

'''
메서드          	용도
count(text)	    text가 문자열 안에 몇 번 나오는지 센다
find(text)	       text가 문자열 안에서 처음 나오는 위치를 찾는다
rfind(text)	    text가 문자열 안에서 처음 나오는 위치를 뒤에서부터 찾는다
lower()	       문자열을 소문자로 변경한 것을 반환한다
upper()	       문자열을 대문자로 변경한 것을 반환한다
replace(a, b)    문자열에서 a를 b로 치환한 것을 반환한다
strip()	       문자열 좌우의 공백 문자를 없앤 것을 반환한다
lstrip()	       문자열 왼쪽의 공백 문자를 없앤 것을 반환한다
rstrip()	       문자열 오른쪽의 공백 문자를 없앤 것을 반환한다
split(text)	    text를 기준으로 문자열을 여러 개로 나눈다
splitlines()	    개행을 기준으로 문자열을 여러 개로 나눈다
isalpha()	       문자열이 문자(알파벳, 한글 등)로만 구성되어 있는지 검사한다
isnumeric()	    문자열이 숫자로만 구성되어 있는지 검사한다
isalnum()	       문자열이 문자와 숫자로만 구성되어 있는지 검사한다
format()        	데이터를 양식화한다 (11.2 텍스트 양식화에서 설명)
'''

book = '안나 카레니나, Leo Tolstoy'
print(book.count('나'))          # '나'가 몇 번 나오는가?


print(book.find('카레'))        # '카레'가 처음 등장하는 위치를 찾음

print(book.find('카레라이스'))    # 찾는 문자열이 없을 때는 -1이 반환

print(book.rfind('나'))         # '나'가 마지막에 등장하는 위치를 찾음

# 대소문자 변경
print(book.lower()) # 소문자로 변경한다
print(book.upper()) # 대문자로 변경한다.
print(book.replace(' ', '-')) # ' ' 를 -로 변경
print(book.replace('니', '라이스 먹')) #'니' 를 '라이스 먹'으로 변경

#공백 제거
text = ' 카페 라테  '
print(text.strip()) # 모든 공백 제거
print(text.rstrip()) # 오른 쪽 공백 제거
print(text.lstrip()) # 왼 쪽 공백 제거

print(book.split(','))  #문자열을 , 기준으로 2개로 나눈다
print(poem.splitlines()) #문자열을 행에 따라서 나눈다


print(poem.splitlines()[0]) # 문자열을 나누고 그중에서 1개를 뽑아올 수 있다

print(('한글').isalpha())      # 문자열이 모두 문자인지 검사: 참

print(('1024').isalpha())      # 문자열이 모두 문자인지 검사: 거짓

print(('1024').isnumeric())    # 문자열이 모두 숫자인지 검사: 참

print(('3.1415').isnumeric())  # 문자열이 모두 숫자인지 검사: 거짓

print(('1학년').isalnum())     # 문자열이 모두 문자 또는 숫자인지 검사: 참


'''
연습문제 4-4 틀린 단어 고치기

'I think, therefore I am.' 이라는 문자열을 'I eat, therefore I am.'으로 치환하여 화면에 출력하는 프로그램을 작성하라.
'''

think = 'I think, therefore I am'

think_to_eat = think.replace('think','eat')

print(think_to_eat)


'''
손님들의 음료 주문 내용을 메모하여 다음과 같이 문자열로 기록해 두었다.

order_memo = """주문1: 아메리카노
주문2: 카페 라테
주문3: 아메리카노, 아메리카노
주문4: 아메리카노, 카페 라테
주문5: 카페 라테, 카페 라테
"""
이 메모에서 주문을 몇 번 받았는지, 아메리카노가 몇 잔 주문되었는지 각각 세어 화면에 출력하는 프로그램을 작성하라.
'''

def count_order_memo(order_memo = """주문1: 아메리카노
주문2: 카페 라테
주문3: 아메리카노, 아메리카노
주문4: 아메리카노, 카페 라테
주문5: 카페 라테, 카페 라테
""",menu = '아메리카노'):
    """메모를 입력받아 주문의 수와 메뉴의 수를 확인하는 함수, 메모와 메뉴를 변경하여 입력할 수 있다."""
    order = '주문'
    order_count = order_memo.count(order)
    menu_count = order_memo.count(menu)
    return order_count,menu_count

print(count_order_memo())

def weekly_count_uncle_bob_uesr(uncle_bob_weekly_user='11월 29일 영석님,혜승님,경욱님',user1 = '만수',user2='혜승님',user3='경욱님',user4='건령님',user5='현재님',user6='영석님'):
    """엉클 밥을 2주일동안 사용한 멤버가 적혀있는 메모와 실제 이용자 이름을 전달받아 개인별 금액을 산출하는 함수"""
    bob_price = 1000
    user1_count_price = uncle_bob_weekly_user.count(user1) * bob_price
    user2_count_price = uncle_bob_weekly_user.count(user2) * bob_price
    user3_count_price = uncle_bob_weekly_user.count(user3) * bob_price
    user4_count_price = uncle_bob_weekly_user.count(user4) * bob_price
    user5_count_price = uncle_bob_weekly_user.count(user5) * bob_price
    user6_count_price = uncle_bob_weekly_user.count(user6) * bob_price
    return user1,user1_count_price,user2,user2_count_price,user3,user3_count_price,user4,user4_count_price,user5,user5_count_price,user6,user6_count_price

print(weekly_count_uncle_bob_uesr())