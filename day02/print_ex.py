
dog = '멍멍이'
cat = '야옹이' 
print(dog, cat, '좋아요!', sep=' ')
print(dog, cat, '좋아요!', sep='')
print(dog, cat, '좋아요!', sep='=>')

print('==========================================')
print(dog, end='와')   #end='\n' -> \n을 삭제하면 엔터 안함
print(cat)

gim = '김밥'
dan = '단무지'
bob = '볶음밥'

# 김밥!!단무지!!볶음밥==>맛있다
print(gim, dan, bob, sep='!!', end='==>맛있다')