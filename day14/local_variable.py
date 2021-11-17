
'''
# 지역 변수
    - 지역변수란 함수 내부에서 만들어진 변수를 말합니다.
    - 지역변수는 함수 내부에서만 사용할 수 있으며,
      함수 호출이 종료되면 메모리에서 자동제거 됩니다.  => 메모리 절약
'''

def info():
    word = '안녕'   # word => 지역변수
    print(word)
    for c in word:
        print(c)

def greeting():
    word = 'hello'
    print(word)

info()      # 함수 호출 => 함수 내부에서는 얼마든지 word(지역변수)를 사용할수있다
greeting()      # 똑같은 변수(word)를 써도 함수가 다르고 일시적이라 충돌이 생기지 않는다

