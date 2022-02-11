from collections import deque

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [1,-1,0,0], [0,0,1,-1]

t = 0
cheeze_cnt = 0
for r in range(N):
    for c in range(M):
        if array[r][c] == 1:
            cheeze_cnt += 1

def bfs():
    q = deque([(0,0)])
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    melting_lst = []
    melting_cnt = 0
    while q:
        r,c = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc]:
                if array[rr][cc] == 0:
                    q.append((rr,cc))
                    visited[rr][cc] = True
                if array[rr][cc] == 1:
                    melting_lst.append((rr,cc))
                    visited[rr][cc] = True
    
    for cheeze in melting_lst:
        array[cheeze[0]][cheeze[1]] = 0
        melting_cnt += 1
    
    return melting_cnt

while cheeze_cnt != 0:
    melting_cnt = bfs()
    cheeze_cnt -= melting_cnt
    t += 1

print(t)
print(melting_cnt)

