N = int(input())
xx = []
yy = []
zz = []

for _ in range(N):
    x, y, z = map(int, input().split())
    xx.append((_+1, x))
    yy.append((_+1, y))
    zz.append((_+1, z))
xx.sort(key=lambda a: a[1])
yy.sort(key=lambda a: a[1])
zz.sort(key=lambda a: a[1])

graph = []

for i in range(len(xx)-1):
    graph.append((xx[i][0], xx[i+1][0], abs(xx[i][1]-xx[i+1][1])))
for i in range(len(yy)-1):
    graph.append((yy[i][0], yy[i+1][0], abs(yy[i][1]-yy[i+1][1])))
for i in range(len(zz)-1):
    graph.append((zz[i][0], zz[i+1][0], abs(zz[i][1]-zz[i+1][1])))

graph.sort(key=lambda a: a[2])

parent = [x for x in range(N+1)]
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

tmpSum = 0

for item in graph:
    if find(item[0]) != find(item[1]):
        union(item[0], item[1])
        tmpSum += item[2]

print(tmpSum)