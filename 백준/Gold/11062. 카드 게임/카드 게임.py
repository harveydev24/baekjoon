import functools

T = int(input())


def solve(turn, i, j):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    if turn % 2:
        dp[i][j] = max(lst[j] + solve(turn+1, i, j-1),
                       lst[i] + solve(turn+1, i+1, j))
        return dp[i][j]
    else:
        dp[i][j] = min(solve(turn+1, i+1, j), solve(turn+1, i, j-1))
        return dp[i][j]


for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    dp = [[-1]*N for _ in range(N)]

    print(solve(1, 0, len(lst)-1))
