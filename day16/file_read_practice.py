
'''
point.txt를 읽어들여서
점수의 총점과 평균을 구한 후
총점과 평균을 적어서 result.txt에 저장
'''

from typing import final


file_path1 = 'D:/isec_ysyy/py_study/point.txt'
try:
    f = open(file_path1, 'r')
    point_str = f.read()

    points = point_str.split(',')    
        
    total = 0
    for n in points:
        total += int(n)
    
    avg = total / len(points)

    print(f'총점: {total}, 평균: {round(avg,2)}')
except:
    print('파일 로드 실패')
finally:
    f.close()


file_path2 = 'D:/isec_ysyy/py_study/result.txt'
try:
    f = open(file_path2, 'w')
    data = f'총점: {total}점, 평균: {round(avg,2)}점'
    f.write(data)       
except:
    print('파일 쓰기 실패')
finally:
    f.close()