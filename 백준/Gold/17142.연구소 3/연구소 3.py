from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
array_original = [list(map(int, input().split())) for _ in range(N)]
array_copy = [[-1]*N for _ in range(N)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

area = 0
virus_lst = []
wall_cnt = 0
possible = False
ans = 10**9

for r in range(N):
    for c in range(N):
        if array_original[r][c] == 1:
            array_copy[r][c] = '-'
            wall_cnt += 1
        if array_original[r][c] == 2:
            array_copy[r][c] = '*'
            virus_lst.append((r,c))

def check():
    for i in range(N):
        for j in range(N):
            if array[i][j] == -1:
                return False
    return True

for virus_pos in list(combinations(virus_lst, M)):
    array = copy.deepcopy(array_copy)
    visited = [[False]*N for _ in range(N)]
    virus_cnt = M
    inactive_virus = len(virus_lst)-M
    t_max = 0
    is_last_inactive = False
    q = deque([])
    for virus in virus_pos:
        q.append((virus[0],virus[1],0))
        visited[virus[0]][virus[1]] = True
        array[virus[0]][virus[1]] = 0

    if check():
        print(0)
        exit(0)

    while q:
        r,c,t = q.popleft()
        if array[r][c] != '*':
            is_last_inactive = False
        for i in range(4):
            rr,cc = r+dr[i],c+dc[i]
            if 0<=rr<N and 0<=cc<N:
                if not visited[rr][cc] and array[rr][cc] != '-':
                    visited[rr][cc] = t + 1
                    if array[rr][cc] != '*':
                        array[rr][cc] = t + 1
                    else:
                        is_last_inactive = True
                        inactive_virus -= 1
                    q.append((rr,cc,t+1))
                    virus_cnt += 1
                    t_max = max(t_max, t+1)
                    if N**2-virus_cnt-inactive_virus == wall_cnt:
                        break
    if is_last_inactive:
        t_max -= 1
    if N**2-virus_cnt-inactive_virus != wall_cnt:
        continue
    else:
        ans = min(ans, t_max)
        possible = True

if possible:
    print(ans)
else:
    print(-1)
    