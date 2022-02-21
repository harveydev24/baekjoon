from collections import deque

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [1,0],[0,1]

def bfs():
    visited = [[False]*N for _ in range(N)]
    q = deque([(0,0)])
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        dist = array[r][c]
        for i in range(2):
            rr, cc = r+dr[i]*dist, c+dc[i]*dist
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc]:
                q.append((rr,cc))
                visited[rr][cc] = True
                if rr == N-1 and cc == N-1:
                    print("HaruHaru")
                    exit(0)

bfs()
print("Hing")
