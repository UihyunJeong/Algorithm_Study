from functools import reduce

# 앞의 x는 바로 직전의 누적
reduce(lambda x, y : x*10 + y , [1,2,3,4,5]) 
# 12345, int

# 누적 합
reduce(lambda x, y : x+y, [1,2,3,4,5])
# 15, int


