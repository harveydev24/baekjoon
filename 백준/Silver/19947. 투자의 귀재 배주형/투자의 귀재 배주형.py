h, y = map(int, input().split())
dp = [-1 for i in range(y+1)]
dp[0] = h


def solve(y):
    if y < 0:
        return 0

    if dp[y] != -1:
        return dp[y]

    dp[y] = max(int(solve(y-1)*1.05),
                int(solve(y-3)*1.2), int(solve(y-5)*1.35))
    return dp[y]


print(solve(y))