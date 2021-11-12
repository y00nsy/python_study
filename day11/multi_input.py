
'''
x = input('>> ').split()
for i in range(len(x)):
    x[i] = int(x[i])
    
print(x)
'''

# map함수 = 일괄적으로 int로 변환 but 리스트 형태는 안됌 -> 리스트 변환 필요
x = list(map(int, input('>> ').split()))
x.sort(reverse=True)
print(x)

