

s1 = '안녕' #자바나 c언어는 홑따옴표를 사용 안함
print(type(s1))

s2 = "잘가"
print(type(s2))

# s3 = "나는 홍길동에게 "도와줘"라고 말했다."  -> X
s3 = ' 나는 홍길동에게 "도와줘"라고 말했다.'
s4 = "Let's go!"
s5 =  "나는 홍길동에게 \"도와줘\"라고 말했다."
print(s5)

file_path = 'c:\\temp\\new.png' # \t 또는 \n으로 인식할수있으니 \\로 입력
print(file_path)

lyrics = '''Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding
Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding
Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding
Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding

butterfly 너를 만난 첫 순간
눈이 번쩍 머린 Stop 벨이 딩동 울렸어

난 말야 멋진놈 착한놈 그런 놈은 아니지만
나름대로 괜찮은 bad boy

너도 마치 butterfly 너무 약해 빠졌어
너무 순해 빠졌어 널 곁에 둬야겠어

더는 걱정마 걱정마 나만 믿어보면 되잖아
니가 너무 맘에 들어 놓칠 수 없는 걸'''

print(lyrics)