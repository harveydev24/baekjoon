import sys
input = sys.stdin.readline
M, N = map(int, input().split())
maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)]
di, dj = [0, -1, 0, 1], [1, 0 ,-1,0]

def dfs(i, j):
    global res
    if i == M-1 and j == N-1:
        return 1
    elif dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = 0
        for k in range(4):
            if 0<=i+di[k] and i+di[k]<M and 0<=j+dj[k] and j+dj[k]<N:
                if maps[i][j] > maps[i+di[k]][j+dj[k]]:
                    dp[i][j] += dfs(i+di[k], j+dj[k])
        return dp[i][j]

dfs(0,0)
print(dp[0][0])