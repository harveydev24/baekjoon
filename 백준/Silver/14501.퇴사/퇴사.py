N = int(input())
work = [(0,0)]
dp = [0] * (N+1) # i일째에 받을 수 있는 최대급여

for i in range(1,N+1):
    T, P = list(map(int, input().split()))
    work.append([T, P])

for i in range(1,N+1):
    tmp = [dp[i-1]]
    for j in range(1,i+1):
        if work[j][0]+j-1 == i:
            if j == i:
                tmp.append(dp[i-1] + work[j][1])
            else:
                tmp.append(dp[j-1] + work[j][1])
    dp[i] = max(tmp)
print(dp[-1])