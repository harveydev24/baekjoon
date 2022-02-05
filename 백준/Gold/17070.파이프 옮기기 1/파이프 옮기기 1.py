import copy

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dp = [[(0,0,0)] * N for _ in range(N)]
for i in range(1,N):
    if array[0][i] != 1:
        dp[0][i] = (1,0,0)
    else:
        break

for i in range(1,N):
    for j in range(N):
        if array[i][j] != 1:
            a,b,c=0,0,0
            if 0<=i-1 and 0<=j-1:
                if array[i-1][j] != 1 and array[i][j-1] != 1:
                    c = sum(dp[i-1][j-1])
            if 0<=i-1:
                b = dp[i-1][j][1] + dp[i-1][j][2]
            if 0<=j-1:
                a = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j] = (a,b,c)

print(sum(dp[N-1][N-1]))