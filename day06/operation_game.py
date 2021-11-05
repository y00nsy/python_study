
print('~~~~~~~~~~ 재미있는 사칙연산 게임 ~~~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~]')
print('='*50)

import random

# 난이도 설정
print('~~~~~~~~~~~~~~ 난이도를 설정합니다 ~~~~~~~~~~~~~~~')
print('[ 1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20) ]')
level = int(input('>> '))

'''
#난이도 랜덤범위 숫자도 바뀌어야함
if level == 1:
    levelNum = 100
elif level == 2:
    levelNum = 50
elif level == 3:
    levelNum = 20
else:
    levelNum = 999
'''

quiz = 1
yes_count = 0
no_count = 0

while True:
    secret1 = random.randint(1,levelNum)
    secret2 = random.randint(1,levelNum)
    secret3 = random.randint(1,3)
    
    if secret3 == 1:
        print(f'Q{quiz}. {secret1} + {secret2} = ??')
        break
    elif secret3 == 2:
        print(f'Q{quiz}. {secret1} * {secret2} = ??')
        break
    else:
        print(f'Q{quiz}. {secret1} - {secret2} = ??')
        break

while True:
    win = int(input('>> '))
    quiz += 1
    if level == 1:
        print(f'Q{quiz}. {secret1} {secret3} {secret2} = ??')    
    elif level == 2:
        print(f'Q{quiz}. {secret1} {secret3} {secret2} = ??') 
    else:
        print(f'Q{quiz}. {secret1} {secret3} {secret2} = ??')
        
    answer = secret1, secret3, secret2

    print(f'Q{quiz}. {secret1} + {secret2} = ??')
    win = int(input('>> '))
    quiz += 1
    if win == 0:
        print('게임을 종료합니다!')
        print('-'*50)
        print(f'정답횟수: {yes_count}회, 틀린횟수: {no_count}회')
        break
    if win == answer:
        print('정답입니다!')
        yes_count += 1
    else:
        print('틀렸습니다~')
        no_count +=1


