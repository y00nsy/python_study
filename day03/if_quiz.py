
score1 = int(input('국어 : '))
score2 = int(input('영어 : '))
score3 = int(input('수학 : '))

avg = (score1 + score2 + score3)/3
# avg = round(avg,2) -> 영구적 반올림
# :.소수점자리수f -> 일시적 반올림
print('당신의 평균점수: {:.2f}점' .format(avg))

if avg >= 60:
    print('이번 시험에 통과하셨습니다.')

else:
    print('재수강 대상자입니다.')

print('열공하세요!')
