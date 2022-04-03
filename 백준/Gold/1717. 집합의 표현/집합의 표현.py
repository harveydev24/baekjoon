import sys
input = sys.stdin.readline
n, m = map(int, input().split())
myList = [x for x in range(n+1)]

def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a != b:
        myList[a] = b

def findParent(a):
    tmp = a
    while a != myList[a]:
        a = myList[a]
    myList[tmp] = a
    return a


for i in range(m):
    method, a, b = map(int, input().split())
    if not method:
        union(a,b)
    else:
        if findParent(a) == findParent(b):
            print('YES')
        else:
            print('NO')