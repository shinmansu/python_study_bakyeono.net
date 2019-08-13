
# 코드 8-1
cordinate = {'x' : 5, 'y': 3}

triangle_1 = {
    'point_a' : {'x':0 , 'y': 0},
    'point_b' : {'x':3 , 'y': 0},
    'point_c' : {'x':3 , 'y': 4}
}

rectangle_1 = {
    'point_a' : {'x':2 , 'y': 2},
    'point_b' : {'x':6 , 'y': 2},
    'point_c' : {'x':6 , 'y': 6},
    'point_d' : {'x':2 , 'y': 6}
}

import math # 제곱근(math.sqrt()) 계산을 위해 수학 모듈 임포트

def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

def distance(point_a, point_b):
    """두 점 사이의 거리를 게산해 반환한다. (피타고라스의 정리)"""
    return math.sqrt(square(point_a['x'] - point_b['x']) +
                     square(point_a['y'] - point_b['y']))


def circumference_of_triangle(shape):
    """삼각형 데이터를 전달 받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_a = distance(shape['point_c'], shape['point_a'])
    return a_to_b + b_to_c + c_to_a

def circumference_of_rectangle(shape):
    """삼각형 데이터를 전달 받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_d = distance(shape['point_c'], shape['point_d'])
    d_to_a = distance(shape['point_d'], shape['point_a'])
    return a_to_b + b_to_c + c_to_d + d_to_a


# 둘레 계산
print(circumference_of_triangle((triangle_1)))  # 12
print(circumference_of_rectangle((rectangle_1))) # 16


cordinate_2 = (3, 5) # 점(좌표)

triangle_2 = ((0, 0), (3, 0), (3, 4)) # 삼각형

rectangle_2 = {
    'point': (2, 2),
    'width': 4,
    'height' : 4,
}

# 유형: '좌표'는 다음 키를 갖는 사전이다.
#     * 'x': x 축의 위치 (정수)
#     * 'y': y 축의 위치 (정수)
coordinate_1 = {'x': 5, 'y': 3}

# 유형: '삼각형'은 다음 키를 갖는 사전이다.
#     * 'point_a': 첫번째 점의 위치 (좌표)
#     * 'point_b': 두번째 점의 위치 (좌표)
#     * 'point_c': 세번째 점의 위치 (좌표)
triangle_1 = {
    'point_a': {'x': 0, 'y': 0},
    'point_b': {'x': 3, 'y': 0},
    'point_c': {'x': 3, 'y': 4},
}

# 유형: '사각형'은 다음 키를 갖는 사전이다.
#     * 'point_a': 첫번째 점의 위치 (좌표)
#     * 'point_b': 두번째 점의 위치 (좌표)
#     * 'point_c': 세번째 점의 위치 (좌표)
#     * 'point_d': 네번째 점의 위치 (좌표)
rectangle_1 = {
    'point_a': {'x': 2, 'y': 2},
    'point_b': {'x': 6, 'y': 2},
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}

# 딕셔너리에 데이터 유형을 추가할 수 있음

triangle_3 = {
    'type': '삼각형',             # 데이터의 유형을 나타내는 정보
    'point_a': {'x': 0, 'y': 0},
    'point_b': {'x': 3, 'y': 0},
    'point_c': {'x': 3, 'y': 4},
}

rectangle_3 = {
    'type': '사각형',             # 데이터의 유형을 나타내는 정보
    'point_a': {'x': 2, 'y': 2},
    'point_b': {'x': 6, 'y': 2},
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}


def circumference(shape):
    """도형 데이터를 전달받아 둘레를 구해 반환한다."""

    if shape['type'] == '삼각형':  # type() 함수 대신 인덱싱 연산 사용
        a_to_b = distance(shape['point_a'], shape['point_b'])
        b_to_c = distance(shape['point_b'], shape['point_c'])
        c_to_a = distance(shape['point_c'], shape['point_a'])
        return a_to_b + b_to_c + c_to_a

    elif shape['type'] == '사각형':  # type() 함수 대신 인덱싱 연산 사용
        a_to_b = distance(shape['point_a'], shape['point_b'])
        b_to_c = distance(shape['point_b'], shape['point_c'])
        c_to_d = distance(shape['point_c'], shape['point_d'])
        d_to_a = distance(shape['point_d'], shape['point_a'])
        return a_to_b + b_to_c + c_to_d + d_to_a

    else:
        return None


print(circumference(triangle_3))  # 12.0
print(circumference(rectangle_3))  # 16.0

# 개념 정리
# 데이터에 데이터의 유형을 나타내는 정보를 추가할 수 있다.
# 데이터의 유형을 구별할 수 있으면 그에 따라 알맞는 연산을 수행할 수 있다.


#연습문제 8-2 체스말, 바둑돌 출력하기

# 연습문제 8-1에서 정의한 체스말 또는 바둑돌 데이터를 전달받아
# 화면에 출력하는 함수 print_piece()를 정의해라. 이 함수는 전달받은 데이터가
# 체스말인지, 바둑돌인지를 식별해 각각 다른 방식으로 출력해야 한다.
# 다음은 이 함수를 실행한 예다.

# >>> print_piece(체스말1)
# black 룩이 A8 위치에 놓여 있어요.
#
# >>> print_piece(바둑돌2)
# 제 84 수: 백이 (12, 3) 위치에 두었습니다.

# 이곳에 체스말 데이터 유형 정의하기
체스말1 = {'type': '체스', 'x': 'A', 'y': '8', 'color': 'black', 'role': '룩'}
체스말2 = {'type': '체스', 'x': 'E', 'y': '1', 'color': 'white', 'role': '킹'}

# 이곳에 바둑돌 데이터 유형 정의하기
바둑돌1 = {'type': '바둑', 'x': 8, 'y': 14, 'order': 83, 'color': '흑'}
바둑돌2 = {'type': '바둑', 'x': 12, 'y': 3, 'order': 84, 'color': '백'}

def check_position(board) :
    if board['type'] == '체스' :
        place = str(board['x'])+str(board['y'])
        color = board['color']
        role = board['role']
        print ( color + ' ' + role + ' ' + place + ' 위치에 놓여 있어요.')
        return
    elif board['type'] == '바둑' :
        place_2 = str(board['x']) + ', ' + str(board['y'])
        color = board['color']
        order  = str(board ['order'])
        print ( '제 ' + order + ' 수: '+ color + '이 ('+ place_2+ ') 위치에 두었습니다.')
        return

check_position(바둑돌1)


