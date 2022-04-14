def cal(n):
    tmp = 1
    ret = 0
    while n >= tmp:
        if n & tmp:
            ret += 1
        tmp = tmp << 1
    return ret


N, K = map(int, input().split())

ans = 0

while True:
    if cal(N) <= K:
        print(ans)
        exit(0)
    ans += 1
    N += 1