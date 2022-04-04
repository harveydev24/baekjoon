n, m = map(int, input().split())
parent = [x for x in range(n+1)]

def find(x):
    tmp = x
    while x != parent[x]:
        x = parent[x]
    parent[tmp] = x
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(m):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print(i+1)
        break
    union(x, y)
else:
    print(0)