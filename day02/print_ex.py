
dog = '멍멍이'
cat = '야옹이' 
print(dog, cat, '좋아요!', sep=' ')  # sep=() 의 기본값은 공백이다
print(dog, cat, '좋아요!', sep='')
print(dog, cat, '좋아요!', sep='=>')

print('==========================================')
print(dog, end='와')   # end='\n' -> \n을 삭제하면 엔터 안함
print(cat)

gim = '김밥'
dan = '단무지'
bob = '볶음밥'

# 김밥!!단무지!!볶음밥==>맛있다
print(gim, dan, bob, sep='!!', end='==>맛있다')

# 탈출 문자 (escape sequence)
# \n : 줄 바꿈, \t : 들여쓰기
print("\n\n안녕하세요!")
print('잘\t가\t\t!!')

# 문자열 포맷팅
print('='*40)

idol = '방탄소년단'
bts = 7

print(idol + '은 ' + str(bts) + '명입니다.') 
print(idol, '은 ', bts, '명입니다.', sep='')

# %s : 문자를 넣을때, %d : 정수, %f : 실수 
print('%s은 %d명입니다.' % (idol, bts))
print('{}은 {}명입니다.'.format(idol, bts))

month = 12
day = 25
anni = '크리스마스'

# 12월 25일은 크리스마스입니다.
print('%d월 %d일은 %s입니다.' % (month, day, anni))
print("{}월 {}일은 {}입니다." .format(month, day, anni))

print("=" * 40)

pi = 3.14159265
# %f : 자동으로 소수점 6자리까지 무조건 제한되어 표시된다
print('원주율은 %f입니다.' % (pi))
print('원주율은 %.8f입니다.' % (pi)) 
# %.숫자f : 원하는 숫자까지 소수점 표시
print('원주율은 {}입니다.' .format(pi))
print('원주율은 {:.2f}입니다.' .format(pi)) # {:.숫자f}

me = 'kim'
you = 'park'
print('{} and {} and {}' .format(me, you, me))
print('{0} and {1} and {0}' .format(me, you))
print('{a} and {b} and {a}' .format(a=me, b=you))

print("=" * 40)

num = 1234
print('~~~~%d~~~~' % num)
print('~~~~%6d~~~~' % num)
print('~~~~%8d~~~~' % num)
print('~~~~%-6d~~~~' % num)
print('~~~~%-8d~~~~' % num)

for p in [30, 19600, 8700, 500, 25]:
    print('가격: %7d원' % p)

print('\n\n')
print('%-9s%-9s%-9s%-9s' % ('번호', '이름', '나이', '부서'))
print("=" * 40)

print('\n\n')

print('~~~~{}~~~~' .format(num))
print('~~~~{:>8d}~~~~' .format(num))  #  오른쪽 정렬
print('~~~~{:>10d}~~~~' .format(num))
print('~~~~{:<8d}~~~~' .format(num))  #  왼쪽 정렬
print('~~~~{:<10d}~~~~' .format(num))
print('~~~~{:^8d}~~~~' .format(num))  # 가운데 정렬
print('~~~~{:^10d}~~~~' .format(num))