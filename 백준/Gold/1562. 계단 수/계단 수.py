N = int(input())

dp = [[0 for _ in range(1 << 10)] for _ in range(10)]

MOD = 1e9

for i in range(1, 10):
    dp[i][1 << i] = 1

for i in range(1, N):
    dp_ = [[0 for _ in range(1 << 10)] for _ in range(10)]
    for j in range(10):
        for k in range(1 << 10):
            if 0 < j < 9:
                dp_[j][k | (1 << j)] += (dp[j+1][k]+dp[j-1][k]) % MOD
            if j == 0:
                dp_[j][k | (1 << j)] += dp[j+1][k] % MOD
            if j == 9:
                dp_[j][k | (1 << j)] += dp[j-1][k] % MOD
    dp = dp_

print(int(sum([dp[i][(1 << 10)-1] for i in range(10)]) % MOD))
