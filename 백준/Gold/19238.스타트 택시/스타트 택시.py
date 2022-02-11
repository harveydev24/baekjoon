from collections import deque

# 입력 받기
N, M, fuel = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(int, input().split())

# 승객의 목적지를 저장하기 위한 딕셔너리
destination = {}

passenger_cnt = M

for _ in range(M):
    r,c,rr,cc = map(int, input().split())
    array[r-1][c-1] = 2 # 승객을 지도 상에 2로 표기
    destination[(r-1,c-1)] = (rr-1,cc-1) # 목적지 저장

# 택시의 현재 위치와 연료를 저장하는 딕셔너리
taxi = {
    'pos': [taxi_r-1, taxi_c-1],
    'fuel': fuel
}

# bfs를 위한 리스트
dr,dc = [1,-1,0,0],[0,0,1,-1]

def findPassengers(r,c):
    q = deque([(r,c,0)])
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    passengers = []
    dist_min = 10**9

    while q:
        r,c,dist = q.popleft()
        if array[r][c] == 2 and dist==0:
            passengers.append((r,c,0))
            break
        if dist >= dist_min:
            break

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and array[rr][cc] != 1:
                q.append((rr,cc,dist+1))
                visited[rr][cc] = True
                if array[rr][cc] == 2:
                    passengers.append((rr,cc,dist+1))
                    dist_min = min(dist_min, dist+1)
    
    passengers.sort()
    if passengers:
        return passengers[0]
    else:
        print(-1)
        exit(0)
def findDestination(r,c,passenger):
    r_dest, c_dest = destination[(passenger[0],passenger[1])]
    q = deque([(r,c,0)])
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True

    while q:
        r,c,dist = q.popleft()
        if r==r_dest and c==c_dest:
            return dist
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and array[rr][cc] != 1:
                q.append((rr,cc,dist+1))
                visited[rr][cc] = True
    print(-1)
    exit(0)



while passenger_cnt>0:
    passenger = findPassengers(taxi['pos'][0], taxi['pos'][1])
    if passenger[2]<=taxi['fuel']:
        array[taxi['pos'][0]][taxi['pos'][1]] = 0
        taxi['pos'][0], taxi['pos'][1] = passenger[0],passenger[1]
        taxi['fuel'] -= passenger[2]
    else:
        print(-1)
        exit(0)
    fuel_required = findDestination(taxi['pos'][0], taxi['pos'][1], passenger)
    if fuel_required<=taxi['fuel']:
        array[taxi['pos'][0]][taxi['pos'][1]] = 0
        taxi['pos'][0], taxi['pos'][1] = destination[(passenger[0],passenger[1])]
        taxi['fuel'] += fuel_required
        passenger_cnt-=1
    else:
        print(-1)
        exit(0)

print(taxi['fuel'])

