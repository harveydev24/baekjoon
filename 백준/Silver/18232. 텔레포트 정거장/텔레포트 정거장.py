from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())


def bfs(x):
    q = deque([x])
    dp[x] = 0

    while q:
        curr = q.popleft()

        if 1 <= curr+1 <= N:
            if dp[curr]+1 < dp[curr+1]:
                dp[curr+1] = dp[curr] + 1
                q.append(curr+1)
        if 1 <= curr-1 <= N:
            if dp[curr]+1 < dp[curr-1]:
                dp[curr-1] = dp[curr] + 1
                q.append(curr-1)

        if adj.get(curr) != None:
            for next in adj.get(curr):
                if dp[curr]+1 < dp[next]:
                    dp[next] = dp[curr]+1
                    q.append(next)


dp = [10**6]*(N+1)

adj = {}

for _ in range(M):
    x, y = map(int, input().split())
    if adj.get(x) == None:
        adj[x] = [y]
    else:
        adj[x].append(y)
    if adj.get(y) == None:
        adj[y] = [x]
    else:
        adj[y].append(x)


bfs(S)
print(dp[E])
