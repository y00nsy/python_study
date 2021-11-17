
sale_rate = 0.8     #=> 전역변수(함수 안밖에서 모두 사용 가능)

def calc_price(price):
    today_price = price * sale_rate
    print(f'오늘의 가격: {today_price}원')

print(sale_rate)
#   print(today_price)  => 지역변수라 함수 밖에서 출력 안됨
#   print(price)  => 지역변수라 함수 밖에서 출력 안됨

# 전역변수의 수정으로 인해 함수 실행결과가 바뀔수있다.(최소한으로 사용해야한다)
sale_rate = 0.6 

calc_price(2000)


money = 1000   #전역변수

def discount():
    # 함수를 통해 전역변수 값에 관여하려면 global키워드 사용하면 된다
    # global money # => 앞으로 이 함수에서는 전역변수 money를 활용하라는 의미

    print('함수discount 실행!')
    money = 500     # 지역변수
    print(f'지역변수 money: {money}')    #함수내부에서는 지역변수가 우선
    print(f'지역변수 money의 메모리주소 값: {hex(id(money))}')

# 같은 이름의 money(함수)여도 다른 곳에 저장됨 서로 다르게 분류됨

discount()

print(f'전역변수 money: {money}')  #지역변수는 메모리에서 지워진다
print(f'전역변수 money의 메모리주소 값: {hex(id(money))}')