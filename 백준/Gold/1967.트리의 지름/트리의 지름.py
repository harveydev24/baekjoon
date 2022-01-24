from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b,dist))
    graph[b].append((a, dist))

def bfs(startNode):
    visited = [-1] * (n+1)
    q = deque([startNode])
    visited[startNode] = 0
    tmpMax, tmpIdx = 0, 0

    while q:
        curr = q.popleft()
        for item in graph[curr]:
            if visited[item[0]] == -1:
                visited[item[0]] = visited[curr] + item[1]
                q.append(item[0])
                if tmpMax <= visited[item[0]]:
                    tmpMax = visited[item[0]]
                    tmpIdx = item[0]
    
    return tmpMax, tmpIdx

tmpMax, tmpIdx = bfs(1)
ans, ansIdx = bfs(tmpIdx)
print(ans)