

# 리스트 인덱싱
tvxq = ['영웅재중', '최강창민', '유노윤호', '믹키유천', '시아준수']
print(tvxq[2])
print(type(tvxq))
print(type(tvxq[0]))

# tvxq.find('재') => tvxq는 리스트타입이라 함수적용이 안된다
# tvxq[0].find('재')

print(tvxq[1].find('창'))
print(tvxq[1][3])
print(tvxq[3][:2])

# 리스트 슬라이싱
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #  == range(10)

print(nums[2:5:1])
print(nums[:4])
print(nums[6:][1])

result = nums[5] + nums[2:7][3]
print(result)

print(type(nums[3]))
print(type(nums[2:5]))

# 리스트는 인덱싱을 통해 변수처럼 내부값을 변경할 수 있습니다
print('=' * 40)

tvxq[2] = '아이노유노'
print(tvxq)

tvxq[4] = tvxq[0][:2]
print(tvxq)

# 문자열은 인덱싱을 통한 수정이 불가능한 리스트입니다.
s = 'hello'
# s[2] = 'x' # hexlo로 변경하고 싶어도 할수 없음. 인덱싱을 통한 변경X
s = s.replace('l','x',1)
print(s)

# unpackaging: 리스트 내부 데이터를 다시 변수에 따로 저장
# 좌항의 변수 개수와 우항의 리스트 데이터 개수가 일치해야 함

# tvxq = ['영웅재중', '최강창민', '유노윤호', '믹키유천', '시아준수']
hero, max, yuno, micky, xia = tvxq
print(max)

'''
hero = tvxq[0]
max = tvxq[1]
yuno = tvxq[2]      #언패키징으로 더 간략하게 할수있음
micky = [3]
xia = [4]
'''

# 리스트의 +과 * 연산
print('=' * 40)
list1 = [1,2,3,4,5]
list2 = [10,11,12]

print(list1 + list2) # 연결해서 이어붙인다
print(list2 + list1)
print(list2 * 3) # 리스트 * 정수 =>만 가능
print(list1)  #원본은 변하지 않음


# 빈 리스트 만들기
empty = []
empty = list()
