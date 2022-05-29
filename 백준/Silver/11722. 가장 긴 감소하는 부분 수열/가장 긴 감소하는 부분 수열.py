N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
ans = 0

for i in range(N):

    tmp_max = 0
    tmp_idx = 0

    for j in range(i):
        if A[j] > A[i]:
            tmp_max = max(tmp_max, dp[j])

    dp[i] = tmp_max + 1
    ans = max(dp[i], ans)

print(ans)