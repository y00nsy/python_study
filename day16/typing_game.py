
import random as r
import time as t    # 시간과 날짜를 제어하는 모듈

# 사운드 출력 모듈
import winsound

# 텍스트 데이터를 읽어서 저장시킬 리스트
word_list = []

# === 함수 정의 부 === #

# 메모장에 있는 단어를 읽어들이는 함수
def read_words():
    file_path = 'D:/isec_ysyy/py_study/resource/word.txt'

    try:
        f = open(file_path, 'r')
        while True:
            w = f.readline()
            if len(w) == 0: break
            # wordlist에서 \n 제거
            word_list.append(w.strip())
    except:
        print('파일 로드 실패')
    finally:
        f.close()

# 문제를 출제 처리 함수
def assign_question(q_list):

    ok_count = 0

    for n in range(len(q_list)):
        print(f'\n# Question {n + 1}')
        print(f'> {q_list[n]}')
        answer = input('> ')

        if answer == q_list[n]:
            print('\n> Right <')
            ok_count += 1

            # 소리 재생
            winsound.PlaySound(
                'D:/isec_ysyy/py_study/sound/good.wav'
                , winsound.SND_FILENAME
                )
        else:
            print('\n> Wrong <')
            winsound.PlaySound(
                'D:/isec_ysyy/py_study/sound/bad.wav'
                , winsound.SND_FILENAME
                )
    
    return ok_count

# 결과를 판정하는 함수
def show_result(cnt, game_time):
    print('\n결과 발표 ')

    t.sleep(3)  # 3초동안 프로그램이 잠시 멈춤
    
    if cnt >= 3:
        print('합격')
    else:
        print('불합격')

    print(f'총 게임시간: {round(game_time, 2)}초, 정답 개수: {cnt}개')

# 게임 시작 함수
def start():
    read_words()
    input('Ready?? Press Enter Key!')

    '''
    # 5문제를 저장할 리스트
    q_list = []
    # 랜덤으로 5문제 추출
    for x in range(5):
        rn = r.randint(0, len(word_list) -1)
        q_list.append(word_list[rn])
    '''

    # 자동으로 중복을 제외한 랜덤 5문제 추출
    q_list = r.sample(word_list, 5)

    # 시간을 재는 함수
    start = t.time()

    # 문제를 출제하는 함수
    ok_count = assign_question(q_list)

    end = t.time()

    # 결과 판정하는 함수
    show_result(ok_count, end - start)


## == 메인 실행부 == ##
if __name__ == '__main__':
    start()