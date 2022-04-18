N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

INF = 10**5

dp = [[INF]*(1 << N) for _ in range(N)]


def solve(person, visited):
    if visited == (1 << N)-1:
        return 0

    if dp[person][visited] != INF:
        return dp[person][visited]

    for i in range(N):
        if visited & (1 << i):
            continue

        dp[person][visited] = min(
            dp[person][visited], solve(person+1, visited | (1 << i))+D[person][i])
    return dp[person][visited]


print(solve(0, 0))
