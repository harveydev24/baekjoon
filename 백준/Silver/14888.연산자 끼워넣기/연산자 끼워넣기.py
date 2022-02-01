from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
operators_ = list(map(int, input().split()))
operators = ['+'] * operators_[0] \
          + ['-'] * operators_[1] \
          + ['*'] * operators_[2] \
          + ['%'] * operators_[3]    

operators = permutations(operators, N-1)

tmpMax = -1000000000
tmpMin = 1000000000

for item in operators:
    tmp = numbers[0]
    for idx in range(N-1):
        if item[idx] == '+':
            tmp += numbers[idx+1]
        elif item[idx] == '-':
            tmp -= numbers[idx+1]
        elif item[idx] == '*':
            tmp *= numbers[idx+1]
        else:
            tmp = int(tmp/numbers[idx+1])
    tmpMax = max(tmpMax, tmp)
    tmpMin = min(tmpMin, tmp)

print(tmpMax)
print(tmpMin)


