import sys
sys.setrecursionlimit(10**5)
N = int(input())
s = input()

numbers = []
operators = []

tmp = ''
for letter in s:
    if letter.isdigit():
        tmp += letter
    else:
        numbers.append(tmp)
        tmp = ''
        operators.append(letter)
if tmp:
    numbers.append(tmp)

ans = -float('inf')

def dfs(idx, sub):
    global ans

    if idx == len(operators):
        ans = max(ans, int(sub))
        return
    first = str(eval(sub + operators[idx] + numbers[idx+1]))
    dfs(idx + 1, first)

    if idx+1<len(operators):
        second = str(eval(numbers[idx+1] + operators[idx+1] + numbers[idx+2]))
        second = str(eval(sub + operators[idx] + second))
        dfs(idx+2, second)

dfs(0, numbers[0])
print(ans)
    