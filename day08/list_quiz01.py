
tvxq = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

print(f'수정전: {tvxq}')
t = input('수정할 이름을 입력: ')


if t in tvxq:
    tvxq.remove(t)
    new_name = input('새로운 이름: ')
    tvxq.append(new_name)
    print('수정 완료!')
    print(f'수정 후: {tvxq}')
    
else:
    print('그런 멤버는 없어~~')




'''
tvxq = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

print('수정전:', tvxq)
old_name = input('수정할 이름을 입력:')

while True:
    if old_name in tvxq:
        new_name = input('새로운이름: ')
        tvxq[tvxq.index(old_name)] = new_name
        print('수정완료')
        print('\n수정후:',tvxq)
        break
    else:
        print('그런멤버는 없어')

'''
