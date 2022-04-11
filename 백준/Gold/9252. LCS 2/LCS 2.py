fisrt = list(input())
second = list(input())

M, N = len(fisrt), len(second)

adj = [[0] * (N+1) for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if fisrt[i-1] == second[j-1]:
            adj[i][j] = adj[i-1][j-1] + 1
        else:
            adj[i][j] = max(adj[i][j-1], adj[i-1][j])
print(adj[M][N])
res = []
i, j = M, N

while True:
    if adj[i-1][j] != adj[i][j] and adj[i][j-1] != adj[i][j]:
        res.append(second[j-1])
        i -= 1
        j -= 1
    else:
        if adj[i-1][j] == adj[i][j]:
            i -= 1
        elif adj[i][j-1] == adj[i][j]:
            j -= 1
    if i == 0 or j == 0:
        break

res=res[::-1]
if adj[M][N] != 0: print(''.join(res))
