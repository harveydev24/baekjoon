from collections import deque

N = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def bfs(x):
    q = deque([(x, 0)])
    visited = [False] * (N+1)
    visited[x] = True
    max_depth_idx = -1
    max_depth = -1

    while q:
        curr, depth = q.popleft()
        if max_depth < depth:
            max_depth_idx = curr
            max_depth = depth

        for next in adj[curr]:
            if not visited[next]:
                visited[next] = True
                q.append((next, depth+1))

    return max_depth, max_depth_idx


_, idx = bfs(1)
ans, _ = bfs(idx)

print((ans)//2 + ans % 2)
