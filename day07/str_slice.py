

s = 'python'

print(s[2:5:1]) #시작인덱스는 포함, 끝인덱스는 포함X
print(s[1:4]) # step 자리 생략하면 1로 처리
print(s[3:]) # 3번부터 끝까지 라는 의미임
print(s[:4]) # 처음부터 4번 미만까지 라는 의미
print(s[:]) # 전체 

print('=' * 40)

week = '월화수목금토일'

print(week[1:6:2])
print(week[::3])

