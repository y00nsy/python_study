
import random

win_lotto = []   # 당첨된 번호리스트

while len(win_lotto) < 6:
    rn = random.randint(1, 45)    # 1~45 난수 생성
    if rn not in win_lotto:
        win_lotto.append(rn)

win_lotto.sort()
# print('당첨번호:', win_lotto)

# 보너스 번호 생성
while True:
    bonus_x = random.randint(1, 45)    # 보너스번호 후보
    if bonus_x not in win_lotto:       # 보너스 번호와 당첨번호가 겹치지 않도록
        bonus = bonus_x
        break
# print(f'보너스 번호: {bonus}')


paper = 0
while True:

    my_lotto = []   # 내가 구매한 번호리스트

    while len(my_lotto) < 6:
        rn = random.randint(1, 45)    # 1~45 난수 생성
        if rn not in my_lotto:
            my_lotto.append(rn)

    my_lotto.sort()
    # print('내 번호:', my_lotto)
    paper += 1

    # =================================================

    count = 0   # 맞춘 개수를 저장
    '''
    for n in my_lotto:
        for m in win_lotto:
            if n == m:
                count += 1
                break
    '''

    for n in my_lotto:
        if n in win_lotto:
            count += 1
    # print(f'맞춘 개수: {count}개')
    
    
    if count == 6:
        print('1등에 당첨되었습니다!')
    else:
        print(f'로또 {paper}장째 구매중......')


'''
# 등수 체크
if count == 6:
    print('1등!')
elif count == 5:
    if bonus in my_lotto:
        print('2등!')
    else:
        print('3등!')
elif count == 4:
    print('4등!')
elif count == 3:
    print('5등!')
else:
    print('꽝!')
'''
