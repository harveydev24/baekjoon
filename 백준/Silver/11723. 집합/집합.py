import sys
input = sys.stdin.readline

mySet = set([])

for _ in range(int(input())):
    tmp = input().split()
    order = tmp[0]
    if len(tmp) == 2:  
        x = int(tmp[1])
    
    if order == 'add':
        mySet.add(x)
    elif order == 'remove':
        mySet.discard(x)
    elif order == 'check':
        if x in mySet:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if x in mySet:
            mySet.discard(x)
        else:
            mySet.add(x)
    elif order == 'all':
        mySet = set([x for x in range(1, 21)])
    elif order == 'empty':
        mySet = set()

        