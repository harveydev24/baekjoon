N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = -10**5

for i in range(N-K+1):
    tmp = 0
    for j in range(i, i+K):
        tmp += arr[j]

    ans = max(ans, tmp)

print(ans)
