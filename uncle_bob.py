def weekly_count_uncle_bob_uesr(uncle_bob_weekly_user='11월 29일 영석님,혜승님,경욱님',user1 = '승현님',user2='혜승님',user3='경욱님',user4='찬중님',user5='기형님',user6='경진님',user7 = '준협님',user8 = '현우님', user9 = '영석님'):
    """엉클 밥을 2주일동안 사용한 멤버가 적혀있는 메모와 실제 이용자 이름을 전달받아 개인별 금액을 산출하는 함수"""
    bob_price = 1500
    user1_count_price = uncle_bob_weekly_user.count(user1) * bob_price
    user2_count_price = uncle_bob_weekly_user.count(user2) * bob_price
    user3_count_price = uncle_bob_weekly_user.count(user3) * bob_price
    user4_count_price = uncle_bob_weekly_user.count(user4) * bob_price
    user5_count_price = uncle_bob_weekly_user.count(user5) * bob_price
    user6_count_price = uncle_bob_weekly_user.count(user6) * bob_price
    user7_count_price = uncle_bob_weekly_user.count(user7) * bob_price
    user8_count_price = uncle_bob_weekly_user.count(user8) * bob_price
    user9_count_price = uncle_bob_weekly_user.count(user9) * bob_price
    return user1,user1_count_price,user2,user2_count_price,user3,user3_count_price,user4,user4_count_price,user5,user5_count_price,user6,user6_count_price,user7,user7_count_price,user8,user8_count_price,user9,user9_count_price

print(weekly_count_uncle_bob_uesr("""2019-01-28 기형님, 혜승님, 경욱님
2019-01-29 기형님,혜승님, 경욱님,찬중님
2019-01-31 영석님, 혜승님,기형님,경욱님,찬중님
2019-02-01 영석님, 혜승님,기형님,찬중님,현우님,경욱님"""))