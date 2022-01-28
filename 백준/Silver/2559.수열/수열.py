N, K = map(int, input().split())
array = list(map(int, input().split()))

ans = -10**9
tmp = 0
for i in range(N):
    tmp += array[i]
    if i == K-1:
        ans = max(ans, tmp)
    if i>=K:
        tmp -=array[i-K]
        ans = max(ans, tmp)
print(ans)
