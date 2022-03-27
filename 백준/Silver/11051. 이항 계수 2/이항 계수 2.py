N, K = map(int, input().split())

ans = 1
for i in range(1, K+1):
    ans *= (N-i+1)
    ans //= i

ans %= 10007
print(ans)
