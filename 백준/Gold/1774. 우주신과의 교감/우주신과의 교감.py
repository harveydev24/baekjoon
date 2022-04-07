import sys
input = sys.stdin.readline
N, M = map(int, input().split())
coor = [-1]
connected = []
distSum = 0
graph = []

parent = [x for x in range(N+1)]
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<=y:
        parent[y] = x
    else:
        parent[x] = y

def dist(coor1, coor2):
    return ((coor1[0]-coor2[0])**2+(coor1[1]-coor2[1])**2)**0.5

for _ in range(N):
    x, y = map(int, input().split())
    for idx, item in enumerate(coor):
        if idx == 0: continue
        graph.append((_+1, idx, dist(coor[idx], (x,y))))
    coor.append((x,y))
graph.sort(key=lambda x: x[2])

for _ in range(M):
    a, b = map(int, input().split())
    union(a,b)

connected = list(set(connected))

res = 0
for item in graph:
    if find(item[0]) != find(item[1]):
        res += item[2]
        union(item[0], item[1])

print("%.2f" %res)