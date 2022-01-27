N = int(input())
lst = []
h_max = 0

for _ in range(N):
    L, H = map(int, input().split())
    lst.append((L, H))
    h_max = max(h_max, H)

stack = []

lst.sort(key=lambda x: x[0])

pass_highest = False

for item in lst:
    if not pass_highest:
        if not stack:
            stack.append(item)
        else:
            if item[1] > stack[-1][1]:
                stack.append(item)
        if item[1] == h_max:
            pass_highest = True
    else:
        if item[1] <= stack[-1][1]:
            stack.append(item)
        else:
            while item[1] > stack[-1][1]:
                stack.pop()
            stack.append(item)

if len(stack) == 1:
    print(stack[0][1])
else:
    area = 0
    for i in range(1, len(stack)):
        area += abs(stack[i][0]-stack[i-1][0])*min(stack[i][1], stack[i-1][1])
    print(area+h_max)