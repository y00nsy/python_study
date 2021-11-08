
#021031-1231234

num = input('주민번호: ')

prontNum = num[0:6]
behindNum = num[7:]
genderNum = int(behindNum[7])

print(f'주민번호 앞자리: {prontNum}')
print(f'주민번호 뒷자리: {behindNum}')

