
name = "홍길동"  #type -> str
score = 78  #type -> int

print(name + "님의 점수는 " + str(score) + "점입니다.")

print(type(score))

n1 = 10
n2 = '34'
print(str(n1) + n2)
print(n1 + int(n2))

# 타입 변환 함수는 일시적 변화일 뿐 실제 값은 변하지 않는다.
print('==========================================')

print(type(n2))

n2 = int(n2)
print(type(n2))

# int('hello') -> 변환 대상이 정수로 바뀔 수 없는 값이면 에러 발생

s = '2.33'
print(float(s)) 

# 반올림 할 때는 round() 함수를 사용
print('==========================================')

print(round(4.78))
print(int(4.78))  # 소수점 버리고 싶을 땐 int함수 사용
print(round(4.18))
print(round(4.67812354646466464, 2))
