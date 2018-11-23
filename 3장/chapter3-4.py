'''
전역변수와 지역변수

전역 이름공간에 정의되어, 프로그램 어디서든 부를 수 있는 이름을 전역변수(global variable)라고 한다.
함수 밖에서 변수를 정의하면 전역변수가 된다. 반면에 지역 이름공간에 정의되어,
그 문맥 속에서만 부를 수 있는 이름을 지역변수(local variable)라고 한다.
모든 함수는 자신만의 지역 이름공간을 가지며, 함수 속에서 작성한 변수는 그 함수의 지역변수가 된다.
'''


# seconds_per_minute = 60 # 1분은 60초
#
# def minutes_to_seconds(minutes):
#     """분을 입력받아 같은 시간만큼의 초를 반환한다."""
#     seconds = minutes * seconds_per_minute #
#     return seconds
#
# print(minutes_to_seconds(3))
# print(seconds) - 에러가 난다 seconds는 함수 안에서 정의된 지역변수이기 때문이다

'''
전역변수는 어디에서나 읽을 수 있지만, 함수 안에서 전역변수에 새로운 값을 대입하는 것은 금지된다. (잠시후 설명할 global 문을 사용하면 예외적으로 가능해진다.) 표 3-1은 지역변수와 전역변수의 접근 조건을 표로 정리한 것이다.

특징	        전역변수	지역변수
함수 안에서 읽기	가능   	가능
함수 안에서 수정	불가(*)	가능
함수 밖에서 읽기	가능	불가
함수 밖에서 수정	가능	불가
'''

'''
전역변수: 함수 밖, 전역 이름공간에 정의된 변수
지역변수: 함수 안, 지역 이름공간에 정의된 변수
지역변수는 그 변수가 정의된 함수 안에서만 읽을 수 있다.
전역변수는 프로그램 어디서든 읽을 수 있다. 단, 함수 안에서 전역변수에 새로운 값을 대입할 수는 없다.
'''

pi = 3.141592653589793

def area_of_circle(radius):
    """원의 반지름(radius)을 입력받아 넓이를 반환한다."""
    area = radius * radius * pi
    return area

def volume_of_cylinder(radius, height):
    """원기둥의 반지름(radius)과 높이(height)를 입력받아
    부피를 반환한다."""
    top_area = area_of_circle(radius)
    volume = top_area * height
    return volume

result = volume_of_cylinder(5, 10)
print(result)

# 전역 변수 pie / result
#지역변수 area / top_area / volume

'''
개념 정리

지역변수를 이용해 그 데이터와 관련된 문제를 함수 내부의 문제로 국한시킬 수 있다.
전역변수를 함수 안에서 수정하는 것은 좋지 않다.
'''

