T = int(input())

for _ in range(T):
    k = int(input())
    pages = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]

    for i in range(k-1):
        dp[i][i+1] = pages[i] + pages[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + pages[j]
            
    
    for d in range(2,k):
        for i in range(k-d):
            j = i + d
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i,j)]
            dp[i][j] += min(minimum)
    print(dp[0][-1])
    