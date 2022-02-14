from collections import deque
def lineDirection(x1,y1,x2,y2):
    if x1==x2:
        return 1 # 세로
    else:
        return 0 # 가로

def check(a,b,c):
    if a<=b:
        if a<=c<=b:
            return True
    else:
        if b<=c<=a:
            return True
    return False

def isCross(x1,y1,x2,y2,x3,y3,x4,y4):
    d1 = lineDirection(x1, y1, x2, y2)
    d2 = lineDirection(x3, y3, x4, y4)
    if d1 == d2:
        if d1 == 1:
            if x1 == x3 and (check(y1,y2,y3) or check(y1,y2,y4)):
                return True
        else:
            if y1 == y3 and (check(x1,x2,x3) or check(x1,x2,x4)):
                return True
    else:
        if d1 == 1:
            if check(y1,y2,y3) and check(x3,x4,x1):
                return True
        else: 
            if check(x1,x2,x3) and check(y3,y4,y1):
                return True
    return False
    

m, n = map(int, input().split())
k = int(input())
graph = [[] for _ in range(k+1)]
x = [[] for _ in range(m+1)]
y = [[] for _ in range(n+1)]
buses = {}
destination = [False]*(k+1)
start = []

for _ in range(k):
    bus_num, x1, y1, x2, y2 = map(int, input().split())
    for bus in buses.keys():
        if isCross(buses[bus][0], buses[bus][1], buses[bus][2], buses[bus][3], x1, y1, x2, y2):
            graph[bus].append(bus_num)
            graph[bus_num].append(bus)

    buses[bus_num] = (x1,y1,x2,y2)

sx,sy,dx,dy = map(int, input().split())

for bus in buses.keys():
    x1,y1,x2,y2 = buses[bus]
    if check(x1,x2,dx) and check(y1,y2,dy):
        destination[bus] = True
    if check(x1,x2,sx) and check(y1,y2,sy):
        start.append((bus,1))

def bfs():
    q = deque(start)
    visited = [False]*(k+1)
    for bus in q:
        visited[bus[0]] = True
        if destination[bus[0]]:
            print(1)
            exit(0)
    
    while q:
        bus, cnt = q.popleft()

        for next_bus in graph[bus]:
            if not visited[next_bus]:
                if destination[next_bus]:
                    print(cnt+1)
                    exit(0)
                q.append((next_bus, cnt+1))
                visited[next_bus] = True
bfs()