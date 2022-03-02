N, K = map(int, input().split())
number = list(input())
stack = [number[0]]

cnt = 0
for i in range(1, N):
    if cnt < K:
        if stack[-1] >= number[i]:
            stack.append(number[i])
        else:
            while cnt < K and stack and stack[-1] < number[i]:
                stack.pop()
                cnt += 1
            stack.append(number[i])
    else:
        stack.append(number[i])

while len(stack) != N - K:
    stack.pop()

print(''.join(stack))

