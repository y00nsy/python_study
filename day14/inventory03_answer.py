
# 세이브파일 관련 모듈
import sys
import os
import pickle

#전역정의부
dir_name = 'D:/isec_ysyy/py_study/inventory/'
file_name = 'inventory.sav'

inventory = [{
    '제품번호': 'a001',
    '제품명': '청소기',
    '가격': 50000,
    '수량': 4,
    '총액': 200000
},
{
    '제품번호': 'a002',
    '제품명': '에어컨',
    '가격': 700000,
    '수량': 6,
    '총액': 420000
},
{
    '제품번호': 'a003',
    '제품명': '냉장고',
    '가격': 1000000,
    '수량': 3,
    '총액': 3000000
}]

#======= 함수정의부 =======#

# 세이브 파일 생성 함수
def save_inventory():
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    try:
        # b모드는 딕셔너리나 리스트같은 객체를 통째로 넣을 때 사용하는 모드
        f = open(dir_name+file_name, 'wb')
        pickle.dump(inventory, f) #리스트를 통째로 세이브파일에 저장
    except:
        print('파일 저장 실패')
    finally:
        f.close()

# 파일 로드 기능 함수
def load_inventory():
    global inventory    # 전역변수 inventory를 활용하라 - global

    try:
        f = open(dir_name+file_name, 'rb')
        inventory = pickle.load(f)
    except:
        print('파일 로드 실패')
    finally:
        f.close()

# 제품번호의 중복을 확인하는 함수
def check_duplicate_code():
    while True:

        code = input('- 제품번호: ')
        flag = False  # 중복 플래그

        # 제품번호 중복검증
        for p in inventory:
            if code == p['제품번호']:

                # 중복된 경우
                print('# 제품번호가 중복되었습니다. 다시 입력하세요.')
                flag = True
                break
        if flag == False:
            return code     # 중복안된 제품번호

        
# 제품등록을 수행하는 함수
def insert_product():       #-> 지역변수라 함수끝나면 삭제됨. 정보 저장해둘 리스트를 전역변수에 만들어줘야한다
    product ={}
    print('\n# 제품 정보 등록을 시작합니다.')

    product['제품번호'] = check_duplicate_code()
    product['제품명'] = input('- 제품명: ')
    product['가격'] = int(input('- 가격: '))
    product['수량'] = int(input('- 수량: '))
    product['총액'] = product['가격'] * product['수량']

    inventory.append(product)
    print('# 제품 등록 완료')
    save_inventory()

# 메뉴를 출력하는 함수
def show_menu():
    print('\n*** 재고 관리 프로그램 ***')
    print('#1. 제품 정보 등록하기')
    print('#2. 모든 제품정보 조회')
    print('#3. 개별 제품정보 조회')
    print('#4. 제품 정보 수정하기')
    print('#5. 제품 정보 삭제하기')
    print('#6. 프로그램 종료하기')

# 프로그램 종료처리 함수
def exit_program():
    import sys
    print('\n# 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return

# 제품정보 출력 머리말 부분
def header_print():
    print('\n\t\t*** 창고 재고 정보 ***')
    print('=' * 60)
    print('{:^8s}{:^8s}{:^8s}{:^8s}{:^10s}'.format('제품번호','제품명','가격','수량','총액'))

    print('=' * 60)


# 모든 제품정보를 출력하는 함수
def print_all_products():
    header_print()

    total_price = 0
    for product in inventory:
        total_price += product['총액']
        print('{:^10s}{:^10s}{:^8d}원{:^6d}개{:^12d}원'.format(product['제품번호'],product['제품명'],product['가격'],product['수량'],product['총액']))
        
    print('=' * 60)
    print(f'\t\t창고 전체 재고 총액: {total_price}원')

# 제품코드를 입력받는 함수
def input_code(msg):
    print(f'# {msg}하실 제품의 번호를 입력하세요.')
    code = input('>> ')
    return code

# 제품번호로 해당 제품을 찾아오는 함수
def get_product(code):
    for product in inventory:
        if code == product['제품번호']:
            return product
    return {}   # if문의 조건에 해당하는걸 못찾을 경우 상징적으로 빈 딕셔너리 리턴

#개별 제품 조회 처리 함수
def search_product():
    code = input_code('조회')
    product = get_product(code)

    if len(product) > 0:
        header_print()
        print('{:^10s}{:^10s}{:^8d}원{:^6d}개{:^12d}원'.format(product['제품번호'],product['제품명'],product['가격'],product['수량'],product['총액']))

    else:
        print('# 존재하지 않는 제품입니다.')

#제품정보 수정 처리 함수
def modify_product():
    code = input_code('수정')
    product = get_product(code)

    if len(product) > 0:
        print('\n# [{}] {} 제품의 정보를 수정합니다'.format(product['제품번호'],product['제품명']))

        print('[ 1. 수량 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
        select = int(input('>> '))

        if select == 1:
            # 딕셔너리 수정: 딕셔너리변수[key] = new_value
            product['수량'] = int(input('- 수정할 수량({}): '.format(product['수량'])))
        elif select == 2:
            product['가격'] = int(input('- 수정할 가격({}): '.format(product['가격'])))
        elif select == 3:
            product['수량'] = int(input('- 수정할 수량({}): '.format(product['수량'])))
            product['가격'] = int(input('- 수정할 가격({}): '.format(product['가격'])))

        else:
            print('# 변경을 취소합니다.')

        #공통 처리(총액 갱신)
        product['총액'] = product['가격'] * product['수량']

    else:
        print('{} 제품코드에 해당하는 제품 정보가 등록되지 않았습니다.' .format(code))
    save_inventory()
            

#제품정보 삭제 처리 함수
def delete_product():
    code = input_code('삭제')
    product = get_product(code)

    if len(product) > 0:
        inventory.remove(product)
        print('{}의 정보삭제가 정상 처리되었습니다.'.format(product['제품명']))

    else:    
        print('[{}] 제품코드에 해당하는 제품 정보가 등록되지 않았습니다.' .format(code))
    save_inventory()





#실행부
if __name__ == '__main__':    
    load_inventory()

    while True:
        show_menu()
        
        menu = int(input('\n메뉴입력>>> '))
        if menu == 1:
            insert_product()
        elif menu == 2:
            print_all_products()
        elif menu == 3:
            search_product()
        elif menu == 4:
            modify_product()
        elif menu == 5:
            delete_product()
        elif menu == 6:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')
            
        input('\n# Enter를 누르면 메뉴로 돌아갑니다.')
