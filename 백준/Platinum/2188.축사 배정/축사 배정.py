N, M = map(int, input().split())
cows = [[] for _ in range(N+1)]
sheds = [0] * (M+1)

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for shed in tmp[1:]:
        cows[i].append(shed)
def dfs(cow):
    global visited
    for shed in cows[cow]:
        if visited[shed] == True: continue
        visited[shed] = True
        if sheds[shed] == 0 or dfs(sheds[shed]):
            sheds[shed] = cow
            return True
    return False

for i in range(1, N+1):
    visited = [False] * (M+1)
    dfs(i)

cnt = 0
for i in sheds:
    if i != 0: cnt += 1
    
print(cnt)