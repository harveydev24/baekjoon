from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]



for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    visited = [False] * (N+1)
    parent = [0] * (N+1)
    q = deque([1])

    while q:
        curr = q.popleft()
        visited[curr] = True
        for next in tree[curr]:
            if not visited[next]:
                q.append(next)
                parent[next] = curr

    for i in range(2, len(parent)):
        print(parent[i])

bfs()