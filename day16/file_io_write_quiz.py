'''
 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하시오. 
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
  기존 작성한 내용을 유지하고 
새로 입력한 내용이 추가되어야 한다. 또한 파일명도 입력받아 저장)

다음은 실행 예제이다.
출력 예시: "저장할 내용을 입력: "
실행 할 때마다 사용자가 입력한 내용이 xxx.txt파일에 추가되어야 한다.
'''
#################################################################

'''
# 내가 저장할 폴더 위치
dir_name =  'D:/isec_ysyy/py_study/'


# 파일 저장 기능 수행
text = input('저장할 내용을 입력: ')

# 예외 처리 필수임
try:
    # 파일 입출력을 실행하는 내장함수 : open(path(저장할 경로), mode(저장할 모드))
    # mode : w모드 - 파일저장, r모드 - 파일로드
    # 저장할 파일명
    file_name = input('파일명: ')

    f = open(dir_name + file_name + '.txt', 'w')

    f.write(text)
    
    if file_name == f:
        n =  open(dir_name + file_name + '.txt', 'a')
        n.write(text)
    
    print('파일 저장 성공!')
except:
    print('파일 저장 실패!')
finally:
    f.close()   # 메모리 자원반납
'''
#################################################################

print("저장할 내용을 입력('그만'이라고 입력시 종료됩니다.) ")
user_input = ""
while True:
    temp = input()
    if temp == '그만': 
        break
    user_input += temp + "\n"
    
f_name = input("파일명을 입력: ")
f_path = "D:/isec_spring1/py_study/{}.txt".format(f_name)

try:
    f = open(f_path, "a", encoding='UTF-8')  # 내용을 추가하기 위해서 'a'를 사용
    
    f.write(user_input)  # 입력된 내용을 줄단위로 구분하기 위해 줄바꿈 문자 삽입
    print("파일 저장 성공!")
except:
    print("파일 저장 실패!")
finally:
    f.close()

