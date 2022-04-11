from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    last_year = list(map(int, input().split()))
    last_order = {}
    for i in range(n):
        last_order[last_year[i]] = i+1
    m = int(input())

    adj = [[0]*(n+1) for _ in range(n+1)]
    indice = [0]*(n+1)

    for i in range(n):
        for j in range(i+1, n):
            adj[last_year[i]][last_year[j]] = 1
            indice[last_year[j]] += 1

    for i in range(m):
        a, b = map(int, input().split())
        if last_order[a] < last_order[b]:
            adj[a][b] = 0
            adj[b][a] = 1
            indice[b] -= 1
            indice[a] += 1
        else:
            adj[a][b] = 1
            adj[b][a] = 0
            indice[b] += 1
            indice[a] -= 1

    ans = []
    q = deque([])
    for i in range(1, n+1):
        if indice[i] == 0:
            q.append(i)

    if len(q) >= 2:
        print('?')
        continue

    while q:
        curr = q.popleft()
        ans.append(curr)
        for i in range(1, n+1):
            if adj[curr][i] == 1:
                indice[i] -= 1
                if indice[i] == 0:
                    q.append(i)

    if len(ans) < n:
        print("IMPOSSIBLE")
    else:
        print(*ans)
