
eng_kor = {'student':'학생', 'peach':'복숭아', 'book':'책'}
print(eng_kor)

# 딕셔너리에 데이터 추가
#   - 저장되어있지 않은 key를 이용해서 데이터를 대입
eng_kor['grape'] = '포도'
print(eng_kor)

# 딕셔너리에 데이터 수정
#   - 저장되어 있는 key를 이용해서 데이터 대입
eng_kor['book'] = '서적'
print(eng_kor)

# 딕셔너리 내부 데이터 삭제
del(eng_kor['student'])
print(eng_kor)

print('=' * 40)

# keys(), values() 함수를 쓰면 => 키 목록과 값 목록을 얻을 수 있음 (리스트형태로)
print(eng_kor.keys())
print(eng_kor.values())

print('=' * 40)

# 딕셔너리의 반복문 처리
# key 값을 뽑아서 반복함
for k in eng_kor:
    print(k)
# value 값 => key값을 이용해서
for k in eng_kor:
    print(eng_kor[k])

# 빈 딕셔너리 만들기
empty_dict = {}
empty_dict = dict()

