import time
C, R = map(int, input().split())
K = int(input())

curr_dir = [0, 1]
visited = [[False]*(R+1) for _ in range(C+1)]

def rotate_dir():
    global curr_dir
    curr_dir = [curr_dir[1], -curr_dir[0]]

x, y = 1, 1
cnt = 1
visited[1][1] = True
while cnt < K:
    if 1<=x+curr_dir[0]<=C and 1<=y+curr_dir[1]<=R and visited[x+curr_dir[0]][y+curr_dir[1]]==False:
        visited[x+curr_dir[0]][y+curr_dir[1]] = True
        x, y = x+curr_dir[0], y+curr_dir[1]
        cnt += 1
    else:
        rotate_dir()
        if visited[x+curr_dir[0]][y+curr_dir[1]] == True:
            print(0)
            exit(0)
        visited[x+curr_dir[0]][y+curr_dir[1]] = True
        x, y = x+curr_dir[0], y+curr_dir[1]
        cnt += 1

print(x, y)

