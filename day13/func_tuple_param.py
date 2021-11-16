
def add2(n1, n2):
    return n1 + n2

def add3(n1, n2, n3):
    return n1 + n2 + n3

# n개(여러개)의 정수를 전달하면 총합을 구해주는 함수 => 묶어서 실행하면 됨
def add_all(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# *변수이름 -> 튜플형식이 됨
def add_all2(*numbers):
    numbers = list(numbers)
    print(type(numbers))
    total = 0
    for n in numbers:
        total += n
    return total

##################################

result = add_all([10,20,30,40,50])      #리스트 형식으로 묶기
print(result)

result = add_all((10,20,30,40,50))      #튜플 형식으로 묶기

result2 = add_all2(100, 300, 100)      #이미 함수정의부에서 *변수이름 -> 튜플형식 => 소괄호 하나 안붙여도 에러 안남
print(result2)