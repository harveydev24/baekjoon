from collections import deque
import sys
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

q = deque([R])
visited[R] = 1
seq = 0
while q:
    curr = q.popleft()
    seq += 1

    visited[curr] = seq
    for next in adj[curr]:
        if not visited[next]:
            q.append(next)
            visited[next] = seq


for i in range(1, N+1):
    print(visited[i])