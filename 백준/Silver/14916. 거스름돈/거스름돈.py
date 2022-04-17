import sys
sys.setrecursionlimit(10**5)

n = int(input())

if n == 1 or n == 3:
    print(-1)
    exit(0)

INF = float('inf')

dp = [INF]*(n+1)


dp[2] = 1
if n >= 5:
    dp[5] = 1


def solve(n):
    if n < 2:
        return INF

    if dp[n] != INF:
        return dp[n]

    dp[n] = min(solve(n-2)+1, solve(n-5)+1)
    return dp[n]


print(solve(n))
