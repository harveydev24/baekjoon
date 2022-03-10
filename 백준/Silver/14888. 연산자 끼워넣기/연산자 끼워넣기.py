N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

tmpMax = -1000000000
tmpMin = 1000000000


def calculate(lst):
    global tmpMax, tmpMin

    tmp = numbers[0]
    for idx in range(N-1):
        if lst[idx] == '+':
            tmp += numbers[idx+1]
        elif lst[idx] == '-':
            tmp -= numbers[idx+1]
        elif lst[idx] == '*':
            tmp *= numbers[idx+1]
        else:
            tmp = int(tmp/numbers[idx+1])
    tmpMax = max(tmpMax, tmp)
    tmpMin = min(tmpMin, tmp)


op = ['+', '-', '*', '/']


def permutation(lst, operators, cnt):
    if cnt == N-1:
        calculate(lst)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            lst.append(op[i])
            permutation(lst, operators, cnt+1)
            operators[i] += 1
            lst.pop()


permutation([], operators, 0)

print(tmpMax)
print(tmpMin)
