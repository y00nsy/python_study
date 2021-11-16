
################################################
# 함수 정의부
def add(n1, n2):
    print(f'{n1}, {n2}')
    return n1 + n2
    # a = 10   =>  함수는 리턴을 만나는 순간 즉시 종료(반복문에서의 break 역할같은거)

def sub(n1, n2):
    res = n1 - n2
    return res

def multi(n1, n2):
    print(f'{n1} x {n2} = {n1 *n2}')    #이 경우 리턴이 필요없음

def infinite_loop():
    while True:
        msg = int(input('>>> '))

        if msg == 0:
            print('break!!')        #while True를 바로 나가버림(반복문 즉시 종료) -> 함수이제끝남으로 감
            break
        elif msg == 1:
            print('continue!!')     #continue 시점에서 위로 올라감
            continue
        elif msg == 2:
            print('return!!')       #함수 즉시 종료 -> 실행부로 감(하하호호,함수이제끝남출력 안함)
            return
        
        print('하하호호')
    print('함수 이제 끝남')


# 예; 사칙연산 결과 4개를 모두 리턴하고 싶다면 -> 리턴 값은 하나로
def operate_all(n1,n2):
    return [n1+n2, n1-n2, n1*n2, n1/n2]     #리스트로 만드는 방법이 있음
    # return [add(n1,n2), sub(n1,n2), n1*n2, n1/n2]  => 함수안에 함수 넣는것도 가능

def operate_all2(n1,n2):
    return {
        'add':add(n1,n2)
        , 'sub':sub(n1,n2)
        , 'mul':n1*n2
        , 'div':n1/n2
    }           # 딕셔너리로 만드는 방법도 있음


################################################
# 실행부
if __name__ == '__main__':
    
    print(add(10, 5))

    result = add(100, 200)
    print(result)

    x = len([1,2,3,4])
    print(x)

    result2 = sub(100, 20)
    print(result2)

    multi(3,7)
    
    result3 = add(add(add(2,3),8),11)
    print(result3)
    
    # add(multi(3,3), sub(20,10)) => 리턴이 없는 함수는 그 값이 -> add 안에 들어갈수없다
    multi(add(4,7), sub(10,4))

    print('=' * 40)
    # infinite_loop()   # 함수 호출~

    result_list = operate_all(10,5)
    print(result_list[2])

    result_list2 = operate_all2(10,5)
    print(result_list2)
    print(result_list2['mul'])
    