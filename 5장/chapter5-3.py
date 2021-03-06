#맵핑


'''
이름 역할을 하는 데이터와 값 역할을 하는 데이터를 짝지어 관리하는 방법을 알아보자.

매핑(mapping)은 키(key) 역할을 하는 데이터와 값(value) 역할을 하는 데이터를 하나씩 짝지어 저장하는 데이터 구조

일상 생활에서도 매핑 데이터 구조를 쉽게 찾아볼 수 있다.

아메리카노: 2500, 카페 라테: 3000, 딸기 주스: 3500
cat: 고양이, hammer: 망치, rainbow: 무지개, book: 책

매핑의 특징

키 데이터와 값 데이터를 짝지어 모아 두는 데이터 저장 방식이다.
데이터를 가리킬 때 순서 대신 키를 이용한다.

파이썬의 매핑 컬렉션으로는 사전(dict), 기본 값 사전(defaultdict) 등이 있다.
이 컬렉션들은 데이터를 저장하고 표현하는 방식에 약간씩 차이가 있지만, 키와 값을 짝지어 저장한다는 점은 모두 똑같다.
'''

#5.3.2 사전

'''
사전은 파이썬의 매핑 컬렉션 가운데 가장 대표적이며 활용도가 높다. 이 책에서는 사전에 대해서만 설명할 것이다. 사전만 잘 알아두어도 파이썬 프로그래밍에 어려움이 없으며, 나중에 다른 매핑 컬렉션을 배우더라도 사전과 큰 차이가 없어 금세 배울 수 있을 것이다.

사전 표현하기
사전은 중괄호({, }) 안에 콜론(:)으로 키-값 쌍을 써넣어 표현한다. 키-값 쌍 각각은 콤마(,)로 구분한다.

{
    키1: 값1,
    키2: 값2,
    키3: 값3,
    ...
}
'''

menu_dict = {
    '아메리카노': 2500,
    '카페 라테': 3000,
    '딸기 주스': 3000,
}

dict_2 = {'아메리카노': 2500, '카페 라테': 3000, '딸기 주스': 3500}

empty_dict = {}  # 빈 사전

'''

코드 5-41 다양한 데이터 유형을 키로 사용하기

{
    1004: 'value',       # 정수 키
    (1, 2, 3): 'value',  # 튜플 키
    'key': 'value',      # 문자열 키
}
연습문제
연습문제 5-10 식재료별 칼로리 사전

다음 표를 참고해 식재료별 칼로리를 식재료_칼로리 라는 이름의 사전으로 정의해 보아라. 이 사전은 음식의 이름을 키로, 칼로리를 값으로 저장한다.

음식	kcal (100 그램 당)
밀가루	364
피망	20.1
올리브	115
돼지고기	242.1
'''
meal_kcal = {'밀가루':364,
             '피망': 20.1,
             '올리브': 225,
             '돼지고기': 242.1}

word_dict = {
'cat': '고양이',
'hammer': '망치',
'rainbow': '무지개',
'book': '책',
}
# print(word_dict)
#
#
# print('cat' in word_dict)      # word_dict에 'cat' 키가 있는지 검사
#
#
# print('dog' not in word_dict)  # word_dict에 'dog' 키가 없음을 검사
#
#
# print('망치' in word_dict)     # ❶ word_dict에 '망치' 키가 있는지 검사
#
# print(len({}))         # 빈 사전의 키-값 쌍의 개수
#
#
# print(len(word_dict))  # word_dict의 키-값 쌍의 개수

# 특이점은 len으로 총 값이 아닌 쌍의 개수를 센다는 것이다


# 딕셔너리는 키에 연결된 '값'을 찾을 수 있다
# print(word_dict['cat'] ) # 사전에서 'cat' 키와 연결된 값 구하기

# print(word_dict['dog'])  # 오류: 사전에 없는 키
#KeyError: 'dog'

#KeyError 오류를 피하고 싶으면 get() 메서드를 사용하면 된다.
# get() 메서드는 키가 있으면 키에 연결된 값을 반환하고,
#  키가 없으면 None이나 기본값으로 지정한 값을 반환한다.

# print(word_dict.get('cat'))   # 키가 있을 경우
# print(word_dict.get('dog'))  # 키가 없을 경우 None 반환
# print(word_dict.get('dog', '동물'))

#사전[키] = 값 표현으로 새로운 키-값 쌍을 추가할 수 있다.
word_dict['moon'] = '달'     # 새로운 키-값 쌍 추가
print(word_dict)

word_dict['cat'] = '야옹이'  # 이미 존재하는 키에 새로운 값을 대입
print(word_dict)  # 내용을 확인해보면...

word_dict.update({'star': '별님', 'moon': '달님'})
print(word_dict)


# 어떤 요소(키-값 쌍)을 삭제하고 싶다면 del 사전[키] 명령을 사용한다.
del word_dict['hammer']   # 'hammer' 키를 삭제
print(word_dict)

word_dict.clear()   # 모든 키를 삭제
print(word_dict)


'''
연습문제 5-11 사전을 이용한 칼로리 계산

연습문제 5-10에서 정의한 식재료별_칼로리 사전을 활용해 칼로리를 계산하는 함수 칼로리()를 정의하라. 
이 함수는 음식의 종류와 섭취량을 매개변수에 전달받아 총칼로리를 반환한다.
단, 전달받은 음식이 식재료별_칼로리 사전에 정의되어 있지 않은 경우에는 None을 반환한다. 
다음은 이 함수를 대화식 셸에서 실행한 예다.
'''

def 칼로리(food = '돼지고기',gram = 500):
    meal_100gram_kcal = {'밀가루': 364,
                 '피망': 20.1,
                 '올리브': 225,
                 '돼지고기': 242.1}
    if meal_100gram_kcal.get(food) != None:
        counted_calorie = meal_100gram_kcal.get(food) * (gram/100)
    else:
        counted_calorie = meal_100gram_kcal.get(food)
    return counted_calorie
print(칼로리('돼지고기',500))
print(칼로리('소고기',300))


'''
연습문제 5-12 칼로리 계산기 확장하기

앞에서 정의한 식재료별_칼로리 사전 또는 칼로리() 함수를 수정하여,
칼로리() 함수가 치즈의 칼로리도 계산할 수 있도록 수정해 보아라. 
참고로 치즈의 칼로리는 402.5 kcal / 100g이다.

사전을 수정하는 것과 함수를 수정하는 것 중 어느 방식이 더 편리한가? 그 이유는 무엇인가?
'''
def 칼로리(food = '돼지고기',gram = 500):
    meal_100gram_kcal = {'밀가루': 364,
                 '피망': 20.1,
                 '올리브': 225,
                 '돼지고기': 242.1}
    meal_100gram_kcal['치즈'] = 402.5
    if meal_100gram_kcal.get(food) != None:
        counted_calorie = meal_100gram_kcal.get(food) * (gram/100)
    else:
        counted_calorie = meal_100gram_kcal.get(food)
    return counted_calorie
print(칼로리('치즈',100))


# 코드 5-39의 메뉴판({'아메리카노': 2500, '카페 라테': 3000, '딸기 주스': 3000})을 사전이 아니라 시퀀스로 표현해 보자.
#
# 코드 5-52 메뉴판의 정보를 리스트로 표현했을 때

price_list = [2500, 3000, 3000]                        # ❶
drink_list = ['아메리카노', '카페 라테', '딸기 주스']  # ❷

menu_dict = dict(zip(drink_list, price_list))
#dict을 중복 변수로 사용할 경우 여기서 에러가 나버림 / 조심해서 쓰자
print(menu_dict)

print(menu_dict.keys())   # 사전의 키 시퀀스
print(menu_dict.values())   # 사전의 값 시퀀스
print(menu_dict.items())  # 사전의 키-값 쌍 시퀀스

'''
5.1 변수만으로 데이터를 관리할 수 있을까에서 알아본 데이터 관리 문제를 다시 떠올려 보자.
정해지지 않은 많은 양의 데이터를 관리해야 하는 문제는 이미 리스트를 이용해 해결해 보았다.
하지만 여전히 이름과 전화번호가 한 덩어리로 관리되지 못하고 분리되어 있는 문제를 해결하지는 못했다.
'''

#코드 5-55 사전으로 연락처 표현하기
phone = {
    'name': '박연오',
    'phone': '01012345678',
}

phone_book = {
    'name': '박연오',
    'phone': '01012345678',
    'email': 'bakyeono@gmail.com',
    'website': 'https://bakyeono.net',
}
contact_list = []  # 연락처를 담는 리스트
contact_list.append({'name': '박연오', 'phone': '01012345678'})  # 새 연락처 추가
contact_list.append({'name': '이진수', 'phone': '01011001010'})  # 새 연락처 추가
print(contact_list[0])    # 첫 번째 연락처 확인
print(contact_list[0]['name'])


#문자열로 데이터 표현하기

# 방식 1: 위치로 구별하기
# [0:3] = 이름 / [3:14] = 전화번호
'박연오01012345678'

# 방식 2: 구분자(,)로 구별하기
# split(',') 메서드로 나눈 후, 첫번째는 이름, 두번째는 전화번호
'박연오,01012345678'

# 방식 3: JSON
# JSON 표기법으로 키와 값 지정하기
'{"name":"박연오","phone":"01012345678"}'