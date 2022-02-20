N, M = map(int, input().split())
employees = [[] for _ in range(N+1)]
works = [0 for _ in range(M+1)]

for i in range(1,N+1):
    i_work = list(map(int, input().split()))
    for work in i_work[1:]:
        employees[i].append(work)

def dfs(i):
    global works, employees
    for work in employees[i]:
        if visited[work]: continue
        visited[work] = True
        if works[work] == 0 or dfs(works[work]):
            works[work] = i
            return True
    return False

for i in range(1,N+1):
    visited = [False]*(M+1)
    dfs(i)

cnt = 0
for work in works:
    if work != 0: cnt += 1

print(cnt)