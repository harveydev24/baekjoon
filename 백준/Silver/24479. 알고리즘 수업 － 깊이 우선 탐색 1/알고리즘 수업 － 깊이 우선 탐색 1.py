import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, R = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort()

visited = [0]*(N+1)
cnt = 1


def dfs(i):
    global cnt
    visited[i] = cnt
    cnt += 1
    for next in adj[i]:
        if not visited[next]:
            dfs(next)


dfs(R)

for i in range(1, N+1):
    print(visited[i])