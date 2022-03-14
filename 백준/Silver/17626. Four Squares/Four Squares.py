n = int(input())

dp = [4] * (n+1)
i = 1
while i**2 <= n:
    dp[i**2] = 1
    i += 1

for i in range(2, n+1):
    j = 1
    while j**2 < i:
        if dp[i-j**2]+1 < dp[i]:
            dp[i] = dp[i-j**2]+1
        j += 1

print(dp[-1])
