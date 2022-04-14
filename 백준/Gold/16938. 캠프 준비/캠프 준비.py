N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

lst = [0]*N


def solve(idx, cnt):
    global ans
    if idx == N:
        if cnt >= 2:
            tmp_max, tmp_min = 0, 10**6
            tmp_sum = 0
            for i in range(N):
                if lst[i] == 1:
                    tmp_max = max(tmp_max, A[i])
                    tmp_min = min(tmp_min, A[i])
                    tmp_sum += A[i]
            if L <= tmp_sum <= R and X <= tmp_max-tmp_min:
                ans += 1
        return

    lst[idx] = 1
    solve(idx+1, cnt+1)
    lst[idx] = 0
    solve(idx+1, cnt)


solve(0, 0)
print(ans)