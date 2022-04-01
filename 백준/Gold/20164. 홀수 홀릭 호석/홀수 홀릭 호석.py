N = int(input())


tmp_max = 0
tmp_min = float('inf')


def solve(N, tmp_sum):
    global tmp_max, tmp_min

    if N < 10:
        tmp_sum += N % 2
        tmp_max = max(tmp_max, tmp_sum)
        tmp_min = min(tmp_min, tmp_sum)
        return
    elif N < 100:
        tmp_sum += (N//10) % 2 + (N % 10) % 2
        solve((N//10+N % 10), tmp_sum)
        return

    cnt = -1
    i = 10
    N_ = N
    while N_ != 0:
        tmp_sum += (N_ % i) % 2
        N_ //= i
        cnt += 1

    for i in range(1, cnt):
        for j in range(i+1, cnt+1):
            solve(N % (10**i)+(N % (10**j))//(10**i)+N//(10**j), tmp_sum)


solve(N, 0)
print(tmp_min, tmp_max)
