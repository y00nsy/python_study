

# 리스트를 이용한 연락처 관리프로그램 구현

namelist = []
phonelist = []


while True:
    print("\n--------연락처 관리 프로그램--------")
    print("1. 연락처 등록")
    print("2. 연락처 검색")
    print("3. 연락처 삭제")
    print("4. 연락처 수정")
    print("5. 모든 연락처 조회")
    print("6. 프로그램 종료")
    print("7. 프로그램 초기화")
    print("-----------------------------------")
    
    menu = int(input("메뉴 입력: "))
    
    if menu == 1:
        
        print("-" * 20)
        print("연락처 등록을 시작합니다.")
        name = input("이름: ")
        phone = input("전화번호: ")
        
        # 입력받은 이름데이터와 전화번호데이터를 각각의 리스트에 추가하세요.
        # 추가완료시 "xxx님 연락처 저장 완료!"를 출력하세요.
        namelist.append(name)
        phonelist.append(phone)
    
        print("%s님 연락처 저장 완료!" % name)

    elif menu == 2:
        
        f_name = input("찾을 이름을 입력하세요: ")
        
        if f_name in namelist:
            # 이름이 리스트 안에서 발견된다면 해당 이름을 통해 인덱스 번호를
            # 추출하여 인덱스를 통해 리스트의 데이터를 출력한다.
            # 출력예시: "이순신의 전화번호는 010-1234-1234입니다."
            idx = namelist.index(f_name)  
            
            print(f'{f_name}남의 전화번호는 {phonelist[idx]}입니다.')  # print("%s의 전화번호는 %s입니다." % (???, ???))

        else:
            print("%s님은 연락처 목록에 없습니다." % f_name)
        
    elif menu == 3:
        f_name = input("삭제할 이름을 입력하세요: ")
         
        if f_name in namelist:
            idx = namelist.index(f_name)
            del(namelist[idx])
            del(phonelist[idx])
            
            print(f'{f_name}님의 정보가 정상적으로 삭제되었습니다.')  # print("%s님의 정보가 정상적으로 삭제되었습니다." % f_name)
            
        else: 
            print("%s님은 연락처 목록에 없습니다." % f_name)
    
    elif menu == 4:
        f_name = input("수정할 이름을 입력하세요: ")

        if f_name in namelist:
            idx = namelist.index(f_name)
            del(namelist[idx])
            del(phonelist[idx])
            
            n_name = input('새로운 이름: ')
            n_phone = input('새로운 번호: ')
            namelist.append(n_name)
            phonelist.append(n_phone)
            
            print('f{n_name}님의 정보가 정상적으로 변경되었습니다.')
        else:
            print("%s님은 연락처 목록에 없습니다." % f_name)
        
        '''
        # 해답
        f_name = input('찾을 이름을 입력하세요: ')
        if f_name in namelist:
            print(f'#{f_name}님의 연락처를 수정합니다.')
            idx=namelist.index(f_name)

            old_phone = phonelist[idx]
            phonelist[idx] = input('새로운 전화번호: ')

            print(f'{f_name}님의 전화번호가 {old_phone}에서 {phonelist[idx]}로 수정되었습니다.')
        else:
            print(f'{f_name}님은 연락처 목록에 없습니다.')
        '''        
    
    elif menu == 5:
        
        
        # for문을 통해 리스트 내부의 모든 인덱스에 접근하여 모든 이름과 연락처 정보를
        # 출력하는 코드를 작성하세요.
        if len(namelist) > 0:
            print("\n========전체 연락처 조회========")
            
            for idx in range(len(namelist)):
                print(f'# {idx+1}. {namelist[idx]} : {phonelist[idx]}')

        else:
            print('\n아직 등록된 데이터가 없습니다. 등록을 먼저 진행하세요!')
        
        
    elif menu == 6:
        print("프로그램을 종료합니다.")
        break

    elif menu == 7:

        print('모든 데이터가 삭제됩니다. [y / n]')
        answer = input('>>')

        if answer.lower()[0] == 'y' or answer == 'ㅛ':
            namelist.clear()
            phonelist.clear()
            print('\n모든 데이터가 초기화 되었습니다.')
        else:
            print('\n초기화를 취소합니다.')


    else:
        print("메뉴를 다시 입력해주세요.")
    
    
    
    
    
    
    
    
    