s = input()
N = len(s)
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 3
    else:
        dp[i][i+1] = 2

for l in range(3, len(s)+1):
    for i in range(len(s)-l+1):
        j = i+l-1
        if s[i] == s[j]:
            dp[i][j] = dp[i][j-1] + dp[i+1][j] + 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]

print(dp[0][-1])
