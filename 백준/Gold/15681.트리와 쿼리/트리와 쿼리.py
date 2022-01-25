from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [1] * (N+1)
visited = [False] * (N+1)
visited[R] = True
def postOrder(node):
    for item in graph[node]:
        if not visited[item]:
            visited[item] = True
            dp[node] += postOrder(item)
    return dp[node]

postOrder(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])
    