import sys
sys.setrecursionlimit(10**5)

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
adj = [[] for _ in range(2*(2*N-1))]
matched = [-1] * 2 * (2*N-1)

# 이분 그래프 만들기
for r in range(N):
    for c in range(N):
        if array[r][c] == 1:
            adj[r-c+N-1].append(r+c+2*N-1)
            adj[r+c+2*N-1].append(r-c+N-1)

def dfs(start):
    if visited[start]: 
        return False
    visited[start] = True

    for node in adj[start]:
        if matched[node] == -1 or dfs(matched[node]):
            matched[start] = node
            matched[node] = start
            return True
    return False

cnt = 0
for i in range(2*N-1):
    visited = [False] * (2*N-1)
    if dfs(i):
        cnt += 1

print(cnt)