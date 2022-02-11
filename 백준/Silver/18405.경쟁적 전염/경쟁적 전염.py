from collections import deque

# 입력 받기
N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus_lst = []

# 현재 존재하는 바이러스 위치 저장
for r in range(N):
    for c in range(N):
        if array[r][c] > 0:
            virus_lst.append((r,c,array[r][c],0)) # 바이러스 위치, 바이러스 숫자, 시간

# 바이러스 숫자가 낮은 순서대로 정렬
virus_lst.sort(key=lambda x:x[2])
# 상하좌우 탐색을 위한 리스트
dr, dc = [1,-1,0,0], [0,0,1,-1]

def bfs():
    q = deque(virus_lst)
    
    while q:
        r, c, virus, t = q.popleft()
        if t == S:
            break
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N:
                if array[rr][cc] == 0:
                    array[rr][cc] = virus
                    q.append((rr,cc,virus,t+1))
bfs()

print(array[X-1][Y-1])