from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))

    for i in range(int(len(info)/2)-1):
        graph[info[0]].append((info[2*i+1], info[2*(i+1)]))
        
def bfs(startNode):
    visited = [-1] * (V+1)
    q = deque([startNode])
    visited[startNode] = 0

    tmpMax, tmpIdx = 0, 0
    while q:
        curr = q.popleft()
        for item in graph[curr]:
            if visited[item[0]] == -1:
                visited[item[0]] = visited[curr] + item[1]
                q.append(item[0])
                if tmpMax < visited[item[0]]:
                    tmpMax, tmpIdx = visited[item[0]], item[0]
    return tmpMax, tmpIdx

maxDist, farNode = bfs(1)
ans, ansNode = bfs(farNode)
print(ans)