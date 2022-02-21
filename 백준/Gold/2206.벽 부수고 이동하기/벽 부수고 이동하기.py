import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
array = [list(input()) for _ in range(N)]
dr, dc = [-1,1,0,0],[0,0,-1,1]

def bfs():
    q = deque([(0,0,1)])
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N-1 and c == M-1:
            print(visited[r][c][wall])
            exit(0)
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M:
                if array[rr][cc] == '1' and wall == 1:
                    visited[rr][cc][0] = visited[r][c][1] + 1
                    q.append((rr,cc,0))
                if array[rr][cc] == '0' and visited[rr][cc][wall] == 0:
                    visited[rr][cc][wall] = visited[r][c][wall] + 1
                    q.append((rr,cc,wall))

bfs()
print(-1)
