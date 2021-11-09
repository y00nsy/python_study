

tvxq = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

'''
#내가 하다 만거
print('삭제전: ', tvxq)
delete_name = input('삭제할 이름을 입력: ')

if delete_name in tvxq:
    print('삭제할 이름을 입력하세요!')
    name = input('> ')
    del(tvxq[tvxq.index(delete_name)]) 


else:
    print(f'{delete_name}는(은) 없는 멤버입니다.')
'''

#해답
print('삭제전: ', tvxq)

while True:
    print('삭제할 이름을 입력하세요!')
    name = input('> ')

    if name in tvxq:
        tvxq.remove(name)
        print('삭제후: ', tvxq)
        break
    else:
        print('{}는(은) 없는 멤버입니다.'.format(name))