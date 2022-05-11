import functools
import sys
sys.setrecursionlimit(10**5)

N = int(input())

dp = [0]*(N+1)


def solve(N):
    if N == 1:
        dp[1] = 1
        return 1

    if dp[N]:
        return dp[N]

    i = 1
    tmp = float('inf')
    ret = float('inf')
    while i ** 2 <= N:
        if i ** 2 == N:
            dp[N] = 1
            return 1
        else:
            tmp = solve(N-i**2)+1
            ret = min(ret, tmp)
        i += 1
    dp[N] = ret
    return ret


print(solve(N))
