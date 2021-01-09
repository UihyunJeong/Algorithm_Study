exp = input().split('-')  # input()
result = 0
for val in exp[0].split('+'):
    result += int(val)

for exp_s in exp[1:]:
    for val in exp_s.split('+'):
        result -= int(val)

print(result)
