'''
1.랜덤 정답이 필요함. 1~100 사이의 정수가 생성해야함
2. 사용자가 정답을 입력할 수있게 해야함
3. 비교후 업인지 다운인지 판단해줌
4. 정답을 맞출떄까지 지속적으로 사용자가 정답을 입력할수있어야한다.
    -> 입력하는코드 + 검사하는 코드 반복해야할필요있다
    -> 근데 반복횟수를 사전에 알기 어려움
    -> 무한루프를 써야겠다
5. 사용자에게 입력값의 범위를 힌트로 알려주고 싶음
    그래서 최소값을 저장할 min, 최대값 max를 가각 만듦
    현재 정답 37이라 가정 , 사용자는 50입력, 다운인 상황
    -> 다음번 범위는 1~50-> 맥스가 사용자의 입력값으로 변경
    현재 정답 37, 사용자는 14입력 -> 업인상황
    -> 다음번 범위 14~50 -> 민이 사용자의 입력값인 14로 변경
6. 정답을 몇번만에 맞췄는지 알려주기
    -> 입력기회가 몇번이었는지 카운팅하면 될것같음
    -> 카운트를 저장할 변수가 필요함
'''
import random

# 게임의 정답: 1~100 사이의 랜덤 정수
secret = random.randint(1, 100)

print('[UP&DOWN게임 = 1~100 사이의 무작위 숫자를 맞춰보세요!]')

min = 1
max = 100
count = 0
count_down = 6 #6번만에 맞추라는 의미

#난이도 설정
print('# 게임의 난이도를 선택하세요.')
print(' [ 1. 상 | 2. 중 | 3. 하 ]')
level = int(input('>>> '))

if level == 1:
    print('난이도 상을 선택했습니다. 기회가 4번 주어집니다.')
    count_down = 4
elif level == 2:
    print('난이도 중을 선택했습니다. 기회가 6번 주어집니다.')
    count_down = 6
elif level == 3:
    print('난이도 하을 선택했습니다. 기회가 8번 주어집니다.')
    count_down = 8
else:
    print('난이도 선택이 잘못되었으므로 상난이도로 자동시작합니다.')
    count_down = 4

while True:
    #카운트다운이 소진됐을때 알림메세지 제공
    if count_down == 0:
        print('승리 기회가 날아갔습니다. 그러나 문제를 계속 풀어주세요!!')

    #사용자의 입력
    if count_down >0:
        answer = int(input(f'\n# 숫자를 입력하세요({min}~{max} | {count_down}): '))
    else:
        answer = int(input(f'\n# 숫자를 입력하세요({min}~{max}): '))

    #범위 안의 값을 입력했는지 검증
    if (min > answer) or (max < answer):
        print('\n# 숫자 범위를 벗어났어요!!')
        continue

    #입력카운트 증가
    count += 1
    count_down -= 1

    if secret == answer:
        print(f'정답입니다!! {count}번만에 맞추셨습니다')
        if count_down > 0:
            print('YOU WIN!!')
        else:
            print('YOU LOSE!!')
        break
    elif secret > answer:
        print('UP!!')
        min = answer
    else:
        print('DOWN!!')
        max = answer