R,C,T = map(int, input().split())
array = []
air_cleaner_pos = []
for i in range(R):
    array.append(list(map(int, input().split())))
    if array[i][0] == -1:
        air_cleaner_pos.append(i)


dr,dc = [1,-1,0,0],[0,0,1,-1]

def difusion():
    difused = []
    for r in range(R):
        for c in range(C):
            if 5 <= array[r][c]:
                amount_of_difusion = array[r][c]//5
                for i in range(4):
                    rr,cc = r+dr[i],c+dc[i]
                    if 0<=rr<R and 0<=cc<C and array[rr][cc] != -1:
                        difused.append((rr,cc,amount_of_difusion))
                        array[r][c] -= amount_of_difusion
    for item in difused:
        array[item[0]][item[1]] += item[2]

def air_clean():
    for r in range(air_cleaner_pos[0]-1,0,-1):
        array[r][0] = array[r-1][0]
    for c in range(C-1):
        array[0][c] = array[0][c+1]
    for r in range(air_cleaner_pos[0]):
        array[r][C-1] = array[r+1][C-1]
    for c in range(C-1,1,-1):
        array[air_cleaner_pos[0]][c] = array[air_cleaner_pos[0]][c-1]
    array[air_cleaner_pos[0]][1] = 0


    for r in range(air_cleaner_pos[1]+1, R-1):
        array[r][0] = array[r+1][0]
    for c in range(C-1):
        array[R-1][c] = array[R-1][c+1]
    for r in range(R-1,air_cleaner_pos[1],-1):
        array[r][C-1] = array[r-1][C-1]
    for c in range(C-1,1,-1):
        array[air_cleaner_pos[1]][c] = array[air_cleaner_pos[1]][c-1]
    array[air_cleaner_pos[1]][1] = 0


for _ in range(T):
    difusion()
    air_clean()

cnt = 0
for r in range(R):
    for c in range(C):
        if array[r][c] > 0:
            cnt += array[r][c]
print(cnt)