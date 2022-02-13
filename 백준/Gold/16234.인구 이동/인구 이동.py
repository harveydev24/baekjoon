N,L,R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [1,-1,0,0],[0,0,1,-1]

def dfs(r,c,n):
    global union, visited
    if union.get(n) == None:
        union[n] = [array[r][c], [(r,c)]]
    else:
        union[n][0] += array[r][c]
        union[n][1].append((r,c))
    visited[r][c] = True

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<N and 0<=cc<N and not visited[rr][cc]:
            if L<=abs(array[r][c]-array[rr][cc])<=R:
                dfs(rr,cc,n)

cnt = 0
while True:
    union = {} # (인구수, [위치])
    visited = [[False]*N for _ in range(N)]
    n = 1
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                dfs(r,c,n)
                n += 1

    if len(list(union.keys())) == N**2:
        print(cnt)
        exit(0)
    else:
        for n, lst in union.items():
            people = lst[0]//len(lst[1])
            for r,c in lst[1]:
                array[r][c] = people
        cnt += 1
