# 전역변수 정의부
inventory =[]

# 함수 정의부

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

    '''
    flag = True
    while flag:
        code = input('- 제품번호: ')
        # 중복 플래그
        flag = False
        # 제품번호 중복검증
        for p in inventory:
            if code == p['제품번호']:
                # 중복된 경우
                flag = True
                break
        product['제품번호'] = code
    # 너무 기니까 중복확인 함수 다시 만들어주는게 좋다
    '''

    product['제품번호'] = check_duplicate_code()
    product['제품명'] = input('- 제품명: ')
    product['가격'] = int(input('- 가격: '))
    product['수량'] = int(input('- 수량: '))
    product['총액'] = product['가격'] * product['수량']

    inventory.append(product)
    print('# 제품 등록 완료')
    

# 메인 실행부
if __name__ == '__main__':
    
    
    while True:
        print('\n1. 제품등록')
        print('2. 전체 제품 조회')
        print('3. 끝내기')
        menu = int(input('>> '))
        if menu == 1:
            insert_product()
        elif menu == 2:
            print(inventory)
        elif menu == 3:
            break