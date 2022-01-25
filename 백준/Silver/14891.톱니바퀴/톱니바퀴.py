def clock(lst):
    return [lst.pop()] + lst

def counterClock(lst):
    return lst[1:] + [lst[0]]


gear = []
for _ in range(4):
    gear.append(list(input()))

def gearCheck(gearNum, direction, visited):
    tmp = gear[gearNum][:]
    visited[gearNum] = True
    if direction == 1: gear[gearNum] = clock(gear[gearNum])
    else: gear[gearNum] = counterClock(gear[gearNum])

    if gearNum-1>=0:
        if gear[gearNum-1][2] != tmp[6] and not visited[gearNum-1]:
            gearCheck(gearNum-1, -direction, visited) 
    if gearNum+1<=3:
        if gear[gearNum+1][6] != tmp[2] and not visited[gearNum+1]:
            gearCheck(gearNum+1, -direction, visited) 

K = int(input())

for _ in range(K):
    visited = [False] * 4
    gearNum, direction = map(int, input().split())
    gearCheck(gearNum-1, direction, visited)

ans = 0
for i in range(4):
    if gear[i][0] == '1':
        ans += 2 ** i

print(ans)




