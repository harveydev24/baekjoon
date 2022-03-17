N, K = map(int, input().split())

bags = [[0 for j in range(K+1)] for i in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if W <= j:
            if bags[i-1][j] <= bags[i-1][j-W]  + V:
                bags[i][j] = bags[i-1][j-W]  + V
            else:
                bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = bags[i-1][j]

print(bags[N][K])

    

