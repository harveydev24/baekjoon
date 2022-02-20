from itertools import product
import copy

N, M = map(int, input().split())
array = []
cctv = []
wall_cnt = 0
for row in range(N):
    tmp = list(map(int, input().split()))
    array.append(tmp)
    for column in range(M):
        if 1<=array[row][column]<6:
            cctv.append([row,column,array[row][column]])
        if array[row][column] == 6:
            wall_cnt += 1

cases = list(product([0,1,2,3], repeat=len(cctv)))

def search(r,c,direction):
    global visited, cnt
    i = 1
    rr, cc = r+i*direction[0], c+i*direction[1]
    while 0<=rr<N and 0<=cc<M:
        if array[rr][cc] == 6:
            break
        else:
            if array[rr][cc] == 0 and not visited[rr][cc]:
                visited[rr][cc] = True
                cnt += 1
            i += 1
            rr, cc = r+i*direction[0], c+i*direction[1]
directinos = [(0,1),(-1,0),(0,-1),(1,0)]
ans = 64
for case in cases:
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(len(cctv)):
        r, c, cctv_num = cctv[i][0],cctv[i][1],cctv[i][2]
        if cctv_num == 1:
            search(r,c,directinos[case[i]])
        elif cctv_num == 2:
            search(r,c,directinos[case[i]])
            search(r,c,directinos[(case[i]+2)%4])
        elif cctv_num == 3:
            search(r,c,directinos[case[i]])
            search(r,c,directinos[(case[i]+1)%4])
        elif cctv_num == 4:
            search(r,c,directinos[case[i]])
            search(r,c,directinos[(case[i]+1)%4])
            search(r,c,directinos[(case[i]+2)%4])
        elif cctv_num == 5:
            search(r,c,directinos[0])
            search(r,c,directinos[1])
            search(r,c,directinos[2])
            search(r,c,directinos[3])
    
    ans = min(ans, N*M-len(cctv)-cnt-wall_cnt)
print(ans)

