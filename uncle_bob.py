def weekly_count_uncle_bob_uesr(uncle_bob_weekly_user='11월 29일 영석님,혜승님,경욱님',user1 = '현식님',user2='혜승님',user3='경욱님',user4='승현님',user5='현우님',user6='영석님',user7 = '기형님'):
    """엉클 밥을 2주일동안 사용한 멤버가 적혀있는 메모와 실제 이용자 이름을 전달받아 개인별 금액을 산출하는 함수"""
    bob_price = 1000
    user1_count_price = uncle_bob_weekly_user.count(user1) * bob_price
    user2_count_price = uncle_bob_weekly_user.count(user2) * bob_price
    user3_count_price = uncle_bob_weekly_user.count(user3) * bob_price
    user4_count_price = uncle_bob_weekly_user.count(user4) * bob_price
    user5_count_price = uncle_bob_weekly_user.count(user5) * bob_price
    user6_count_price = uncle_bob_weekly_user.count(user6) * bob_price
    user7_count_price = uncle_bob_weekly_user.count(user7) * bob_price
    return user1,user1_count_price,user2,user2_count_price,user3,user3_count_price,user4,user4_count_price,user5,user5_count_price,user6,user6_count_price,user7,user7_count_price

print(weekly_count_uncle_bob_uesr("""11월 29일 혜승님, 경욱님
12월 3일 건령님,혜승님
12월 4일 혜승님,경욱님, 기형님
12월 5일 혜승님,경욱님,기형님
12월 10일 혜승님,기형님
12월 11일 혜승님,경욱님
12월 12일 무료제공
12월 13일 승현님, 혜승님,기형님,현식님,경욱님
12월 14일 현식님,경욱님,기형님,현우님"""))