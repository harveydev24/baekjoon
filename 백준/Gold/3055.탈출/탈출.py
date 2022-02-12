from collections import deque

R, C = map(int, input().split())
array = [list(input()) for _ in range(R)]
water_lst = []

for r in range(R):
    for c in range(C):
        if array[r][c] == '*':
            water_lst.append((r,c,0))
        if array[r][c] == 'S':
            pos = (r,c)

dr,dc = [1,-1,0,0],[0,0,1,-1]

def flood_bfs():
    q = deque(water_lst)
    
    while q:
        r,c,t = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<R and 0<=cc<C:
                if array[rr][cc] == '.':
                    q.append((rr,cc,t+1))
                    array[rr][cc] = t+1

def bfs():
    q = deque([(pos[0],pos[1],0)])
    visited = [[False]*C for _ in range(R)]
    visited[pos[0]][pos[1]] = True

    while q:
        r,c,t = q.popleft()
        for i in range(4):
            rr,cc = r+dr[i],c+dc[i]
            if 0<=rr<R and 0<=cc<C and not visited[rr][cc] and array[rr][cc] != '*' and array[rr][cc] != 'X':
                if array[rr][cc] == 'D':
                    print(t+1)
                    exit(0)
                elif array[rr][cc] == '.':
                    q.append((rr,cc,t+1))
                    visited[rr][cc] = True
                elif t+1 < array[rr][cc]:
                    q.append((rr,cc,t+1))
                    visited[rr][cc] = True

flood_bfs()
bfs()
print('KAKTUS')
    