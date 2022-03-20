N = int(input())
INF = int(1e9)
adj = [[] for _ in range(N)]
dp = [[INF]*(1 << N) for _ in range(N)]


def dfs(curr, visited):
    if visited == (1 << N)-1:
        return adj[curr][0] if adj[curr][0] else INF

    if dp[curr][visited] != INF:
        return dp[curr][visited]

    for i in range(N):
        if not adj[curr][i]:
            continue
        if visited & (1 << i):
            continue

        dp[curr][visited] = min(dp[curr][visited], dfs(
            i, visited | (1 << i)) + adj[curr][i])
    return dp[curr][visited]


for i in range(N):
    tmp = list(map(int, input().split()))
    adj[i] = (tmp)

print(dfs(0, 1))
