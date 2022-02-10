N,M,K = map(int, input().split())

ans = 0
for i in range(K+1):
    girls = N - i
    boys = M - (K-i)
    ans = max(ans, min(girls//2,boys))
print(ans)