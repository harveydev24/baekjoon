from itertools import combinations
from collections import deque
import copy
N, M = map(int, input().split())
array_original = [list(map(int, input().split())) for _ in range(N)]
array_only_wall = [[0]*N for _ in range(N)]
dr, dc = [1,-1,0,0], [0,0,1,-1]
virus_pos = []
area = 0

for r in range(N):
    for c in range(N):
        if array_original[r][c] == 2:
            virus_pos.append((r, c))
        if array_original[r][c] != 1:
            area += 1
            array_only_wall[r][c] = -1
        if array_original[r][c] == 1:
            array_only_wall[r][c] = '-'

test_cases = combinations(virus_pos, M)

def bfs(case):
    q = deque([])
    for item in case:
        q.append((item[0],item[1],0))
        visited[item[0]][item[1]] = True
    t_max = 0
    virus_cnt = M

    while q:
        r, c, t = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N:
                if not visited[rr][cc] and array[rr][cc] != '-':
                    array[rr][cc] = t + 1
                    q.append((rr,cc,t+1))
                    visited[rr][cc] = True
                    t_max = max(t_max, t+1)
                    virus_cnt += 1
    
    return t_max, virus_cnt


t_min = 10**9

for case in test_cases:
    array = copy.deepcopy(array_only_wall)
    visited = [[False]*N for _ in range(N)]
    t, virus_cnt = bfs(case)

    if virus_cnt != area:
        continue
    
    t_min = min(t_min, t)

if t_min == 10**9:
    print(-1)
else:
    print(t_min)




    
