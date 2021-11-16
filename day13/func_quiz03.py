
'''
* 연습1 - n개의 정수를 전달받아 평균값을 구하여 
      리턴하는 함수를 작성하세요. (get_avg)
* 연습2 - n개의 정수를 전달받아 가장 큰 숫자를 찾아 
      리턴하는 함수를 작성하세요. (get_max)

힌트) 최대값을 저장할 변수를 선언하고 튜플의 데이터를
      반복하여 서로 비교한 후 최대값 발견시 변수에 저장. 
'''

####################
def get_max(*numbers):
    numbers = data_list
    return max(data_list)


####################



print("-" * 40)

data_list = list(map(int, input("정수: ").split(" ")))

print("최대값: {}".format(get_max(data_list)))