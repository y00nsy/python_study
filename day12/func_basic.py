
total = 0
for n in range(1, 6):
    total += n
print(f'1~5까지의 누적합: {total}')
######## 코드 400줄가량 더 쳤다고 가정 ########
# 400줄 어딘가에서 쓴 코드를 또 쓰게 될 때 계속 반복되는 코드 쓰기 불편
# 또 수정하기 불편함 코드 찾아서 고쳐야 하는데 ...

total = 0
for n in range(1, 101):
    total += n
print(f'1~100까지의 누적합: {total}')
#######################################################

# 함수의 정의   
# 예: (1 ~ x까지의 총합을 구하는 함수)
def calc_total(x):
    print('함수 calc_total 실행')
    total = 0
    for n in range(1, x+1):
        total += n
    return total

print('#' * 50)

# 함수는 정의한 것만으로는 실행되지 않음
# 반드시 호출을 통해 실행시켜야 함 (필요한 시점에서 부르는것: 호출)

num = calc_total(10) # 10이 x로 들어감 => calc_total값은 55가 됨 => 변수 num에 그 값을 넣어줌
print(f'1~10까지의 총합: {num}')

####################################################################

num = calc_total(100)
print(f'1~10까지의 총합: {num}')

print('=' * 40)
############################################

# len()함수 직접 구현
def length(list):
    count = 0
    for x in list:
        count += 1
    return count

n_list = [10,40,90,100,500]
sss = 'hello!!!'

print(f'사용자 정의 함수 length(n_list): {length(n_list)}')
print(f'파이썬 내장함수 len(n_list): {len(n_list)}')

print(f'사용자 정의 함수 length(sss): {length(sss)}')
print(f'파이썬 내장함수 len(sss): {len(sss)}')