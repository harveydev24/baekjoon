n = int(input())
m = int(input())

INF = float('inf')
dp = [[INF]*(n) for _ in range(n)]
route = [[-1]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c
        route[a-1][b-1] = a-1

for k in range(n):
    dp[k][k] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                route[i][j] = route[k][j]

for i in range(n):
    for j in range(n):
        if dp[i][j] == INF:
            dp[i][j] = 0


for item in dp:
    print(' '.join([str(x) for x in item]))

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            print(0)
        else:
            jj = j
            tmp = []
            while jj != i:
                tmp.append(jj+1)
                jj = route[i][jj]

            print(len(tmp)+1, i+1, *tmp[::-1])
