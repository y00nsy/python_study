
import sys

all_food = {}

while True:

    print('\n\n====== 음식점 메뉴 관리 프로그램 ======')
    print('# 1. 신규 메뉴 등록하기')
    print('# 2. 메뉴판 전체보기')
    print('# 3. 프로그램 종료하기')
    print('=======================================')

    menu = input('# 메뉴입력: ')

    if menu == '1':
        menuName = input('메뉴명: ')
        price =input('가격: ')
        print(f'신규 메뉴 {menuName}(이)가 등록되었습니다.')
        all_food[menuName] = price
        
    elif menu == '2':

        print('=======메뉴판=======')
        
        for food in all_food:
            print(f'{food} : {all_food[food]}')
        
        print('====================')
        print('1.수정 | 2.삭제 | 3.나가기')
        change = input('=> ')

        if change == '1':
            print('가격을 변경할 메뉴의 이름을 입력하세요.')
            changeMenu = input('=> ')
            if changeMenu not in all_food:
                print(f'{changeMenu}는(은) 등록된 메뉴가 아닙니다.')
            else:
                changePrice = input('변경할 가격: ')
                print(f'{changeMenu}의 가격이 {changePrice}으로 변경되었습니다.')
                        
        elif change == '2':
            print('삭제할 메뉴명을 입력하세요.')
            del_menu = input('=> ')
            if del_menu not in all_food:
                print(f'{del_menu}는(은) 등록된 메뉴가 아닙니다.')
            else:
                print(f'{del_menu}이(가) 삭제되었습니다.')
                del(all_food[del_menu])
        else:
            continue

            

    elif menu == '3':
        print('# 프로그램을 종료하시겠습니까? [ Y / N]')
        choice = input('=> ')
        if choice.lower()[0] == 'y':
            print('프로그램을 종료합니다.')
            sys.exit()
        else:
            print('종료를 취소합니다.')
            continue

    else:
        print('메뉴를 잘못입력했습니다.')


    input('\n메뉴를 보시려면 Enter ...')