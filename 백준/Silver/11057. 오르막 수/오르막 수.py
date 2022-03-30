N = int(input())

dp = [[-1]*(10) for _ in range(N+1)]


def asc(n, size):
    if size == 1:
        return 10-n

    if dp[size][n] != -1:
        return dp[size][n]

    ret = 0
    for i in range(n, 10):
        ret += asc(i, size-1)

    dp[size][n] = ret

    return ret


print(asc(0, N) % 10007)
