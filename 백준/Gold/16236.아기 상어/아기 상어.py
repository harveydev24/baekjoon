from collections import deque

N = int(input())
array = []

shark = {
    'pos': (0,0),
    'size': 2,
    'fish': 0
}

for row in range(N):
    array.append(list(map(int, input().split())))
    for col, item in enumerate(array[row]):
        if item == 9:
            shark['pos'] = (row, col)

t = 0
dx, dy = [1,-1,0,0],[0,0,1,-1]

def bfs(x,y):
    global array,t,shark
    visited = [[False]*N for _ in range(N)]
    q = deque([(shark['pos'][0], shark['pos'][1], 0)])
    visited[shark['pos'][0]][shark['pos'][1]] = True
    t_min = float('inf')
    fish_lst = []

    while q:
        curr = q.popleft()
        if curr[2]>t_min: break

        for i in range(4):
            xx,yy = curr[0]+dx[i],curr[1]+dy[i]
            if 0<=xx<N and 0<=yy<N and visited[xx][yy] == False:
                if 0<=array[xx][yy]<=shark['size']:
                    q.append((xx,yy,curr[2]+1))
                    visited[xx][yy] = True
                    if 0<array[xx][yy]<shark['size']:
                        if t_min >= curr[2]+1:
                            t_min = curr[2]+1
                            fish_lst.append((xx,yy))
    
    fish_lst.sort()

    if not fish_lst:
        print(t)
        exit(0)
    else:
        array[shark['pos'][0]][shark['pos'][1]] = 0
        shark['pos'] = fish_lst[0]
        t += t_min
        array[fish_lst[0][0]][fish_lst[0][1]] = 9
        shark['fish'] += 1
        if shark['fish'] == shark['size']:
            shark['fish'] = 0
            shark['size'] += 1
    


while True:
    bfs(shark['pos'][0],shark['pos'][1])


