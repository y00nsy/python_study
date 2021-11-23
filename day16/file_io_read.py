

file_path = 'D:/isec_ysyy/py_study/hello.txt'

try:
    f = open(file_path, 'r')
    data = f.read()   #단점 :데이터 용량크면 메모리 부담 큼
    print(data)
except:
    print('파일 로드 실패!')
finally:
    f.close

print('='* 40)
try:
    f = open(file_path, 'r')    # encording = 'utf-8'
    
    '''
    str = f.readline()      # 첫번째줄 읽음
    f = open(file_path, 'r')    # encording = 'utf-8'
    str = f.readline()      # 두번째줄 읽음
    '''

    while True:
        str = f.readline()
        if len(str) == 0: break
        print(str, end = '')
    print(str)
except:
    print('파일 로드 실패')
finally:
    f.close