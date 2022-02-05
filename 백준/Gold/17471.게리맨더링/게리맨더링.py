from itertools import combinations
from collections import deque

N = int(input())
popularity = [0]
graph = [[] for _ in range(N+1)]
tmp_popularity = list(map(int, input().split()))
popularity.extend(tmp_popularity)
total_popularity = sum(popularity)

def bfs(lst):
    visited = [False] * (N+1)
    q = deque([lst[0]])
    
    while q:
        curr = q.popleft()
        visited[curr] = True
        for node in graph[curr]:
            if visited[node] == False and node in lst:
                q.append(node)
    
    for node in lst:
        if visited[node] == False:
            return False
    return True

for i in range(1,N+1):
    info = list(map(int, input().split()))
    graph[i].extend(info[1:])

tmp_min = 2000

for i in range(1,N//2+1):
    lst = list(combinations([x for x in range(1,N+1)], i))
    for A in lst:
        B = []
        for node in range(1,N+1):
            if node not in A:
                B.append(node)
        if bfs(A) and bfs(B):
            A_sum = 0
            for node in A:
                A_sum += popularity[node]
            diff = abs(total_popularity - 2*A_sum)
            tmp_min = min(tmp_min, diff)

if tmp_min < 2000:
    print(tmp_min)
else:
    print(-1)
