N = int(input())
expression = list(input())
num = [int(input()) for _ in range(N)]
stack = []

for item in expression:
    if item.isalpha():
        stack.append(num[ord(item)-65])
    else:
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '-':
            stack.append(-stack.pop() + stack.pop())

        elif item == '*':
            stack.append(stack.pop() * stack.pop())

        elif item == '/':
            stack.append(1/(stack.pop() / stack.pop()))

print('%.2f' % (stack[0]))
