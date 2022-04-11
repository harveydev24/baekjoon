from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0]*(N+1)
ans = [1]*(N+1)
adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B] += 1

q = deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append((i, 1))

while q:
    curr, t = q.popleft()

    for next in adj[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append((next, t+1))
            ans[next] = t + 1

print(*ans[1:])
