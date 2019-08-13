# 함수 정의하기

'''
대출을 신청할 때 우리는 대출 신청 과정을 일일이 말한다면 불편할 것이다

대출 신청 하기가 홈페이지에서 대출 신청을 조회하고 서류를 제출하는 과정인이라는 것을
매번 설명한다면 시간도 오래 걸리고 힘들 것이다

대출 신청하기가 위 내용 처럼 일련의 과정임을 약속하는 것을 함수 정의라고 할수 있다

함수를 정의할 때는 def 문을 사용한다

def 함수이름():       # ❶ 헤더 행
    함수의 내용       # ❷ 내용 행 (여러 행)
'''
#예시는 자판기가 주문을 처리하는 과정이다

# def order():                               # 끝에 콜론(:)을 빠트리지 않도록 주의
#     '''사용자로부터 주문할 음료수를 입력받는다. '''
#     print('주문하실 음료를 알려주세요')    # 이 블록은
#     drink = input()                        # 앞에서부터 네 칸씩
#     print(drink, '주문하셨습니다.')        # 들여쓰기한다
#
# order()
#
# def inputabs():
#     """사용자로부터 정수를 입력받아 절대값을 출력한다."""
#     print('정수를 입력하세요.')
#     intinput = int(input())
#     print(intinput,'의 절대값:',abs(intinput))
#
# inputabs()
#
# def print_price(num_drink):                       # ❶ 매개변수(num_drink) 정의
#     """음료의 잔 수(num_drink)를 전달받아,
#     가격을 화면에 출력한다."""
#     price_per_drink = 2500                        # 한 잔 당 가격 지역변수
#     total_price = num_drink * price_per_drink     # ❷ num_drink에 전달된 값 사용 지역변수
#     print('음료', num_drink, '잔:', total_price)  # ❸
#
# print_price(3)
#
# def print_order(drink, cake):            # ❶ 콤마(,)로 구분해 매개변수 여러 개 정의
#     """음료(drink)와 케익을(cake)를 전달받아,
#     주문 내용을 화면에 출력한다."""
#     print('음료:', drink, '/', '케익:', cake)
#
# print_order('카페라테', '치즈케익')      # ❷ 함수에 여러 개의 인자를 전달하여 호출하기
# print_order('당근케익', '우유')          # ❸ 전달하는 인자의 순서에 주의하자!

'''개념 정리

인자: 함수를 호출할 때 함수에 전달하는 데이터
매개변수: 함수에 전달된 데이터가 대입되는 변수
함수를 호출할 때, 인자·매개변수의 개수·순서가 서로 같아야 한다.
'''

'''
두 가지 출력을 구별하자

함수는 데이터를 화면에 출력하기도 하고, 함수 바깥으로 출력하기도 한다.
둘 다 ‘출력(output)’이라고 불리곤 하지만, 정확하게 표현하면 전자는
프린트(print)’이고, 후자는 ‘반환(return)’이다. 
프린트는 데이터를 사람에게 보여주기 위한 것이다.
반환은 프로그램의 진행을 위해 계산 결과를 함수를 호출한 지점으로 전달하는 것이다.

대화식 셸에서 함수를 실행하면 함수의 출력(반환)이 자동으로 화면에 출력(프린트)된다. 
대화식 셸이 여러분을 위해 함수의 반환값을 화면에 프린트해주기 때문이다. 
실제 프로그램에서는 print() 함수로 화면에 출력하도록 명령한 것만 화면에 프린트된다.

개념 정리

return 문을 이용하여 함수에서 값을 출력(반환)할 수 있다.
return 문이 실행되면 함수의 실행이 종료된다.
None은 값이 없음을 나타내는 값이다. 함수의 반환값을 지정하지 않으면 None이 반환된다.

return - 함수에 반환값을 돌려줘서 함수(매개변수)를 값으로 쓸 수 있게 해준다 

'''
#
# def no_return():
#     """화면에 메시지를 출력하지만, 값을 반환하지는 않는다."""
#     print('이 함수에는 반환값이 없습니다.')
#
# result = no_return()
#
# def triangle_area(base,height):
#     '''삼각형 밑변의 길이를 앞에, 높이를 뒤에 적어줍니다 '''
#     print("삼각형의 넓이는",(base*height)/2,"입니다")
#
# triangle_area(10,8)


# help(minus_8)
# Help on function minus_8 in module __main__:
#
# minus_8(x)
#     정수 x를 입력받아 8을 뺀 값을 반환한다.
# #HELP에 함수를 넣으면 해당 함수의 설명을 볼 수 있다




#연습문제 3-6 매개변수와 반환값이 있는 함수 정의하기


# def average_of_4_numbers(a=512,b=64,c=256,d=192):
#     print((a+b+c+d)/4)
#     pass
# average_of_4_numbers()
#
# def no_return():
#     """화면에 메시지를 출력하지만 , 값을 반환하지는 않는다. """
#     print('이 함수에는 반환값이 없습니다.')
#
# result = no_return()
# print(result)

def triagnle_area(base=10,height=8):
    calculated_triangle_area = base*height/2
    return calculated_triangle_area

print(triagnle_area())
