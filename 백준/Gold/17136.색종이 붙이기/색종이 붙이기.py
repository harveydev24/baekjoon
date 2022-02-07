import copy

array = [list(map(int, input().split())) for _ in range(10)]
papers = {}
for i in range(1,6):
    papers[i] = 5
cnt_min = 30

def check(r,c):
    for n in range(2,6):
        for i in range(r,r+n):
            for j in range(c,c+n):
                if not(0<=i<10) or not(0<=j<10) or array[i][j] != 1:
                    return n-1
    return 5

def stickUnstick(r,c,n,state):
    for i in range(r, r+n):
        for j in range(c, c+n):
            array[i][j] = (state+1)%2

def dfs(r,c,cnt):
    global cnt_min
    if r>=9 and c>9:
        cnt_min = min(cnt_min, cnt)
    
    if cnt >= cnt_min: return

    if c>9:
        dfs(r+1,0,cnt);
        return
    
    if array[r][c] == 1:
        n = check(r,c)
        for i in range(1, n+1):
            if papers[i] >= 1:
                stickUnstick(r, c, i, 1)
                papers[i] -= 1
                dfs(r,c+1,cnt+1)
                stickUnstick(r, c, i, 0)
                papers[i] += 1
    else:
        dfs(r, c+1, cnt)

dfs(0,0,0)

if cnt_min == 30:
    print(-1)
else:
    print(cnt_min)
