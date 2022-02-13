N = int(input())
orders = []
q = []

for _ in range(N):
    orders.append(input().split())

def push(n):
    global q
    q.append(n)

def pop():
    global q
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])
        q = q[1:]

def size():
    global q
    print(len(q))

def empty():
    global q
    if len(q) == 0:
        print(1)
    else:
        print(0)

def front():
    global q
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])

def back():
    global q
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])

for item in orders:
    if len(item) == 2:
        push(int(item[1]))
    else:
        if item[0] == 'pop':
            pop()
        elif item[0] == 'size':
            size()
        elif item[0] == 'empty':
            empty()
        elif item[0] == 'front':
            front()
        elif item[0] == 'back':
            back()
