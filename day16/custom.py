
inch = 2.54     # 1인치에 대한 cm값 저장

# 인치를 cm으로 변환해주는 함수
def convert_inch_to_cm(number):
    return number * inch 

def info():
    print('안녕 메롱')
    
#########################################
print('__name__의 값(외부파일.py):', __name__)

# 내부에서는 __main__
# 외부에서는 custom
# 내부에서 내부실험테스트용으로 사용함
# 외부에서 실행 안되기 때문 : if __name__ == '__main__'

# 실행 테스트
if __name__ == '__main__':

    print('__name__의 값(custom.py):', __name__)


    print(convert_inch_to_cm(1))
    info()
    info()
    info()
    info()