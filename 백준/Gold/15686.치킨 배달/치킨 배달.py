from itertools import combinations
from tabnanny import check

N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

dist = []

chickens = []
houses = []
cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            houses.append((i,j))
        if array[i][j] == 2:
            chickens.append((i,j, cnt))
            cnt += 1

for house in houses:
    tmp = []
    for chicken in chickens:
        tmp.append(abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
    dist.append(tmp)

check_list = list(combinations(chickens, M))

ans = float('inf')
for lst in check_list:
    tmp = 0
    for house in dist:
        t = float('inf')
        for chicken in lst:
            t = min(t, house[chicken[2]])
        tmp += t
    ans = min(ans, tmp)
print(ans)
