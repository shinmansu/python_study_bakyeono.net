# 4.4 참과 거짓

'''4.4.1 불리언
True와 False의 데이터 유형은 불리언(boolean, 줄여서 bool)이라고 부른다.
영국의 논리학자 조지 불(George Boole, 1815-1864)의 이름을 따 만든 용어다.'''


'''4.4.2 논리연산
AND 연산 - 그리고 좌변과 우변의 값이 모두 참어야만 참이고 둘 중 하나가 거짓일 경우
거짓이 된다. 
'''
#
# print(True and True) # 좌변과 우변이 모두 참이어야 함
# print(True and False) # 둘 중 하나라도 거짓이면 거짓
# print(True and True and True) # 여러번 연산할 수 있다
# print(1+1 == 2 and 3 < 4) #여러 등식을 함께 평가할 때 도 활용


#OR

# print(True or False) # 좌변과 우변 중 하나라도 참이면 참
# print(False or False) # 둘 다 거짓이면 거짓
# print(False or False or True) # 여러 번 연산할 수 있다
# print(False or True and True) # and 와 or를 연이여 연산해도 된다

'''
좌변	    우변	    and 연산결과	    or 연산결과
True	True	    True	    True
True	False   	False   	True
False	True	    False	    True
False	False	    False   	False
'''

# not 연산 
# 마지막으로 not 연산은 참을 거짓으로, 거짓을 참으로 뒤집는 연산

# print(not True)
# print(not False)
# print(True and not False)

'''
값	    데이터 유형	의미
False	불리언	    거짓
None	None        유형	값 없음
0   	정수	        0
0.0	    실수	        0
0j	    복소수	    0
''	    문자열     	빈 문자열
()	    튜플      	빈 튜플
[]	    리스트	    빈 리스트
{}	    집합	        빈 집합
dict()	사전	        빈 사전
'''

# print(bool(0))
# print(bool(1))
# print(bool(None))

'''
연습문제 4-7 불리언 연산 연습

다음 연산의 결과를 예상해 보고, 대화식 셸에 입력해 확인해 보아라.

not(True and True or False)
bool(10 < 20 and 0)
bool(False or 1)
'''

print(not(True and True or False))
print(10 < 20 and 0)
print(False or 1)