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

dict = {
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
             '올리브': 225
             '돼지고기': 242.1}
