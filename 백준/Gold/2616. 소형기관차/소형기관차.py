N = int(input())
lst = list(map(int, input().split()))
K = int(input())
asum = [lst[0]]
for i in range(1, N):
    asum.append(asum[-1]+lst[i])

dp = [0]*(N)
dp[K-1] = asum[K-1]
for i in range(K, N):
    dp[i] = max(dp[i-1], asum[i]-asum[i-K])

dp2 = [0]*(N)
dp2[2*K-1] = asum[2*K-1]
for i in range(2*K, N):
    dp2[i] = max(dp2[i-1], dp[i-K]+asum[i]-asum[i-K])

dp3 = [0]*N
dp3[3*K-1] = asum[3*K-1]
for i in range(3*K, N):
    dp3[i] = max(dp3[i-1], dp2[i-K]+asum[i]-asum[i-K])

print(dp3[-1])