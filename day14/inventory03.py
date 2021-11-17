#전역정의부
inventory =[]

#함수정의부

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



#실행부
if __name__ == '__main__':
    
    while True:
        print('\n*** 재고 관리 프로그램 ***')
        print('#1. 제품 정보 등록하기')
        print('#2. 모든 제품정보 조회')
        print('#3. 개별 제품정보 조회')
        print('#4. 제품 정보 수정하기')
        print('#5. 제품 정보 삭제하기')
        print('#6. 프로그램 종료하기')
        
        menu = input('\n메뉴입력>>> ')
        if menu == '1':
            insert_product()
        elif menu == '2':
            print('\n >>> 창고 재고 정보')
            print('=' * 60)
            print('제품번호    제품명    단가    수량    제품총액')
            print('=' * 60)
            print('{} {}    {}원    {}개    {}원'.format())
            print(inventory)
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        elif menu == '5':
            pass
        elif menu == '6':
            break
            
