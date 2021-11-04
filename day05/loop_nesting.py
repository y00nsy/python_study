''''
n = 1
for i in range(3):
    for j in range(4):
        print(f'안녕{n}')
        n += 1
'''

for level in range(2, 10):
    for line in range(1, 10):
        print(f'{level} x {line} = {level*line}')
    print('===================')

for i in range(3):
    for j in range(2):
        print(f'({i}, {j})')
