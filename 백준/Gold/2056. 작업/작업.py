from collections import deque

N = int(input())

adj = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]
t = [0]*(N+1)
indegree = [0]*(N+1)
ans = 0

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    t[i] = lst[0]
    indegree[i] = lst[1]

    for j in range(2, 2+lst[1]):
        adj[lst[j]].append(i)
        adj2[i].append(lst[j])

q = deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append((i, t[i]))

while q:
    curr, time = q.popleft()
    t[curr] = time
    ans = max(time, ans)
    for next in adj[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            max_time = 0
            for prev in adj2[next]:
                if t[prev] > max_time:
                    max_time = t[prev]
            q.append((next, max_time + t[next]))

print(ans)
