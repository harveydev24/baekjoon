N,M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
cloud = [[False]*N for _ in range(N)]
cloud[N-1][0] =  True
cloud[N-1][1] =  True
cloud[N-2][0] =  True
cloud[N-2][1] =  True

orders = [list(map(int, input().split())) for _ in range(M)]

dr,dc = [0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]

def move(d,s):
    lst = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == True:
                ii,jj = i+dr[d-1]*s,j+dc[d-1]*s
                lst.append(((ii+25*N)%N,(jj+25*N)%N))
                cloud[i][j] = False
    for i,j in lst:
        cloud[i][j] = True


def check(r,c):
    dr,dc = [-1,-1,1,1],[-1,1,-1,1]
    cnt = 0
    for i in range(4):
        rr, cc = r+dr[i],c+dc[i]
        if 0<=rr<N and 0<=cc<N:
            if array[rr][cc] > 0:
                cnt += 1
    return cnt
    
def rain():
    lst = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == True:
                array[i][j] += 1
                lst.append((i,j))

    for item in lst:
        array[item[0]][item[1]] += check(item[0],item[1])

    for i in range(N):
        for j in range(N):
            if array[i][j] >= 2 and cloud[i][j] == False:
                array[i][j] -= 2
                cloud[i][j] = True
    
    for item in lst:
        cloud[item[0]][item[1]] = False
    

for order in orders:
    move(order[0], order[1])
    rain()

ans = 0
for i in range(N):
    for j in range(N):
        ans += array[i][j]
        
print(ans)
