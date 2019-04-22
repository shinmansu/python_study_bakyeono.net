
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
    a_to_b = distance(shape['point_a'], shape[point_b])
    b_to_c = distance(shape['point_b'])