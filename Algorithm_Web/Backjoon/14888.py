from itertools import permutations
N = input()
nums = [int(n) for n in input().split()]
operators = []
for o, n in zip(['+', '-', '*', '//'], input().split()):
    operators += [o]*int(n)

operators_per = list()
for item in set(permutations(operators)):
    operators_per.append(item)

def calc(nums, operator) :
    val = nums[0]
    for num, o in zip(nums[1:], operator):

        if val < 0 and o == '//':
            val *= -1
            val = eval('{} {} {}'.format(val, o, num))
            val *= -1
        else :
            val = eval('{} {} {}'.format(val, o, num))
    return val

vals = list(map(lambda x : calc(nums,x), operators_per))
print(max(vals), min(vals))
