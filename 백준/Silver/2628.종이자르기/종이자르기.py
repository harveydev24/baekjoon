w, h = map(int, input().split())
n = int(input())

horizon = [0]
vertical = [0]

for _ in range(n):
    dir, coor = map(int, input().split())
    if dir: # 세로
        horizon.append(coor)
    else: # 가로
        vertical.append(coor)

horizon.append(w)
vertical.append(h)

horizon.sort()
vertical.sort()

horizon = [horizon[i]-horizon[i-1] for i in range(1,len(horizon))]
vertical = [vertical[i]-vertical[i-1] for i in range(1,len(vertical))]


ans = 0
for item in horizon:
    for item2 in vertical:
        ans = max(ans, item*item2)
print(ans)