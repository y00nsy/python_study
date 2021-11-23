
# import random
from random import randint, sample  # from import 사용하면 뒤의 수식에 random. 생략할수있다

rn = randint(1,45)
print(f'rn: {rn}')

foods = ['짜장면', '볶음밥', '김치찌개', '샌드위치', '김밥']
selected = sample(foods, 2)
print(selected)

print('=' * 40)

# from import 사용불가능한 경우
# 2개의 평균
def mean(n1, n2):
    return (n1+n2) /2;
#함수 이름이 겹칠때

# from statistics import mean, variance, stdev
# import statistics
import statistics as st     # 별칭을 붙여 간략하게 사용할수있다

numbers = [35,44,99,100,33,55,66]
print('평균:', st.mean(numbers))
print('분산:', st.variance(numbers))
print('표준편차:', st.stdev(numbers))