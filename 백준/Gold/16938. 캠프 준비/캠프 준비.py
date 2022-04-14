N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(1 << N):
    tmp_sum = 0
    tmp_max, tmp_min = 0, 10**6

    for j in range(N):
        if i & (1 << j):
            tmp_max = max(tmp_max, A[j])
            tmp_min = min(tmp_min, A[j])
            tmp_sum += A[j]

    if L <= tmp_sum <= R and X <= tmp_max-tmp_min:
        ans += 1

print(ans)