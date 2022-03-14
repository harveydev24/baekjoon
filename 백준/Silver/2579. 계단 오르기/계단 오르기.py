N = int(input())
scores = [int(input()) for _ in range(N)]
if N == 1:
    print(scores[0])
elif N == 2:
    print(sum(scores))
else:
    dp = [0]*N
    dp2 = [0]*N
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp2[1] = scores[1]

    for i in range(2, N):
        dp[i] = dp2[i-1]+scores[i]
        dp2[i] = max(dp2[i-2]+scores[i], dp[i-2]+scores[i])
    print(max(dp[-1], dp2[-1]))
