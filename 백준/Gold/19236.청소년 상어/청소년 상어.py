import copy
array = [[] for _ in range(4)]

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        array[i].append([info[2*j],info[2*j+1]-1])

dr, dc = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]

# 상어 입장
ans = array[0][0][0]
array[0][0] = [-1, array[0][0][1]]

def move_fish(r,c):
    global array
    d = array[r][c][1]
    for i in range(8):
        rr, cc = r+dr[(d+i)%8],c+dc[(d+i)%8]
        array[r][c][1] = (d+i)%8
        if 0<=rr<4 and 0<=cc<4:
            if array[rr][cc][0] >= 0:
                array[rr][cc], array[r][c] = array[r][c], array[rr][cc]
                return

def move_fishes():
    global array
    n = 1
    
    while n <=16:
        next = False
        for r in range(4):
            for c in range(4):
                if array[r][c][0] == n:
                    move_fish(r,c)
                    next = True
                    break
            if next:
                break
        n += 1

def find_target(sr,sc,sd):
    target_lst = []
    for i in range(1,4):
        rr, cc = sr+dr[sd]*i, sc+dc[sd]*i
        if 0<=rr<4 and 0<=cc<4 and array[rr][cc][0]>0:
            target_lst.append((rr,cc))
    return target_lst


def dfs(sr,sc,sd,n):
    global ans, array
    ans = max(ans, n)
    move_fishes()
    target_lst = find_target(sr, sc, sd)
    
    array_ = copy.deepcopy(array)
    for x,y in target_lst:
        tmp_n = array[x][y][0]
        n += tmp_n
        array[sr][sc] = [0,0]
        array[x][y] = [-1, array[x][y][1]]
        dfs(x,y,array[x][y][1],n)
        n -= tmp_n
        array = copy.deepcopy(array_)

dfs(0,0,array[0][0][1],ans)
print(ans)