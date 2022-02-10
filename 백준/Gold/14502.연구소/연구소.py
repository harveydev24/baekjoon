from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
array_orinal = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [1,-1,0,0], [0,0,1,-1]
wall_cnt= 0
zero_lst = []
virus_lst = []

for r in range(N):
    for c in range(M):
        if array_orinal[r][c] == 1:
            wall_cnt += 1
        elif array_orinal[r][c] == 0:
            zero_lst.append((r,c))
        else:
            virus_lst.append((r,c))

cases = list(combinations(zero_lst, 3))

def bfs(r,c):
    q = deque([(r,c)])
    visited[r][c] = True
    virus_cnt = 1
    while q:
        curr = q.popleft()
        for i in range(4):
            rr, cc = curr[0]+dr[i], curr[1]+dc[i]
            if 0<=rr<N and 0<=cc<M:
                if not visited[rr][cc] and array[rr][cc] == 0:
                    q.append((rr,cc))
                    array[rr][cc] = 2
                    virus_cnt += 1
                    visited[rr][cc] = True
    return virus_cnt

safe_cnt = 0

for case in cases:
    visited = [[False]*M for _ in range(N)]
    array = copy.deepcopy(array_orinal)
    virus_cnt = 0
    for r,c in case:
        array[r][c] = 1

    for virus in virus_lst:
        if not visited[virus[0]][virus[1]]:
            virus_cnt += bfs(virus[0],virus[1])
    
    safe_cnt = max(safe_cnt, M*N-virus_cnt-wall_cnt-3)
print(safe_cnt)
