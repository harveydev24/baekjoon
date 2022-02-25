from multiprocessing.connection import answer_challenge
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = []

for _ in range(N):
    s = input().rstrip()
    tmp = []
    for letter in s:
        if letter.isdigit():
            tmp.append(int(letter))
        else:
            tmp.append(letter)
    array.append(tmp)

visited = [[False]*M for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dr, dc = [-1,1,0,0], [0,0,1,-1]

def dfs(r,c,cnt):
    global ans
    isOver = True

    for i in range(4):
        rr, cc = r+dr[i]*array[r][c], c+dc[i]*array[r][c]
        if 0<=rr<N and 0<=cc<M:
            if not visited[rr][cc]:
                if array[rr][cc] == 'H':
                    ans = max(ans, cnt)
                    continue
                else:
                    if cnt+1 > dp[rr][cc]:
                        visited[rr][cc] = True
                        isOver = False
                        dp[rr][cc] = cnt+1
                        dfs(rr,cc,cnt+1)
                        visited[rr][cc] = False
            else:
                print(-1)
                exit(0)
    
    if isOver:
        ans = max(ans, cnt)

ans = 0

dfs(0,0,1)
print(ans)
