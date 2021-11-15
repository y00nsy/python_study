
# 매개변수(parameter): 인수를 저장하기 위해 함수정의부에 선언된 변수
# 인수(arguments): 함수호출부에서 함수정의부로 전달되는 데이터

def get_items(weapon,armor):
    weapon_log = f'{weapon} 무기를 획득했습니다.\n'
    armor_log = f'{armor} 방어구를 획득했습니다.'
    return weapon_log + armor_log

message = get_items('목검', '누더기옷')
print(message)

print(get_items('대검', '철갑옷'))
print(get_items('장궁', '비단옷'))

print('=' * 40)

# 매개변수가 없는 함수

# 예) 게시판 글 x개를 가져오는 함수
def get_board_article():
    return '게시글을 30개 가져옵니다.'

print(get_board_article())
print(get_board_article())