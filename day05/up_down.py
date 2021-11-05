import random

print('[UP & DOWN 게임 - 1~100사이의 숫자 중 어떤 숫자가 들어있을까요??]')
print('-'*30)

rn = random.randint(1, 100)

x = 1
y = 100
chance = 6
count = 0

while True:
    num = int(input(f'숫자를 입력하세요({x} ~ {y}): '))
    if num < x or num >y:
        print('숫자 범위를 벗어났어요!!')
        continue
    count += 1
    if num > rn:
        y = num
        print('DOWN!!')
        print(f'정답 기회 {chance}번 남음~~')
    elif num < rn:
        x = num
        print('UP!!')
        print(f'정답 기회 {chance}번 남음~~')
    else:
        print(f'정답입니다!! {count}번만에 맞추셨군요~')
        print('YOU WIN!!')

