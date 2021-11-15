
# 집합(set)
# 순서가 없이 빠르게 저장, 중복저장 허용 X
# [] -> 리스트 |  () -> 튜플  |  {} -> 딕셔너리(key:value)
names = {'허준', '신사임당', '권율', '홍길동', '허준'}  # => 집합
print(type(names))
print(len(names))
print(names)    # 빠른 저장 순서 포기(정해진 순서 없음)

# for문 가능: 리스트, 튜플, 딕셔너리, 셋, 문자열
for x in names:
    print(x)

# 빈 집합 만들기
s = {}
print(type(s))

s = set()
print(type(s))

# set에 데이터 추가/삭제
asia = {'한국', '중국', '일본'}
print(asia)

asia.add('태국')
asia.add('중국')    #중복이라 추가 안됨
print(asia)

# 지울 때
asia.remove('일본')
print(asia)

# 결합(합집합) => update 함수
asia2 ={'이라크', '싱가포르','한국'}
asia.update(asia2)
print(asia)