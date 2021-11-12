import random

win_lotto = []   # 당첨된 번호리스트
bonus_num = 0

while len(win_lotto) < 6:
    rn = random.randint(1, 45)    
    if rn not in win_lotto:
        win_lotto.append(rn)


# 보너스 번호 생성
while True:
    bonus = random.randint(1, 45)    # 보너스번호 후보
    if bonus not in win_lotto:       # 보너스 번호와 당첨번호가 겹치지 않도록
        bonus_num = bonus
        break


# 앞에서부터 1등 당첨 횟수 ~ 5등횟수 + 꽝횟수
prize = [0,0,0,0,0,0]


paper = 0
my_lotto = []   # 내가 구매한 번호리스트

while True:

    cnt = 0     # 일치번호 횟수
    num = random.randint(1,45)

    if num not in my_lotto:
        my_lotto.append(num)

    if len(my_lotto) == 6:
        paper += 1

        for n in my_lotto:
            if n in win_lotto:
                cnt += 1
        
        if cnt == 6:
            prize[0] += 1
        elif cnt == 5:
            if bonus_num in my_lotto:
                prize[1] += 1
            else:
                prize[2] += 1
        elif cnt == 4:
            prize[3] += 1
        elif cnt == 3:
            prize[4] += 1
        else:
            prize[5] += 1

        print('로또 %d장 구매 ... '% paper)

        my_lotto.clear()

        if prize[0] == 1:
            break


print('==================================================')
print('당첨 횟수     당첨시 수령액(세후,평균)    누적 당첨금     당점 확률')

print('1등: %d번     %d원    %d원    5.6f%%'
    %
(prize[0],1500000000,prize[0]*1500000000,(prize[0]/paper)*100))

print('2등: %d번     %d원    %d원    5.6f%%'
    %
(prize[1],1500000000,prize[1]*1500000000,(prize[1]/paper)*100))

print('3등: %d번     %d원    %d원    5.6f%%'
    %
(prize[2],1500000000,prize[2]*1500000000,(prize[2]/paper)*100))

print('4등: %d번     %d원    %d원    5.6f%%'
    %
(prize[3],1500000000,prize[3]*1500000000,(prize[3]/paper)*100))




print('==================================================')

print('누적 사용 금액 : {}원')
print('누적 당첨금 총합 : {}원')
print('순이익 : {}원')
print('수익률 : {}%')
