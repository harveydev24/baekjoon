N, K = map(int, input().split())
kit = list(map(int, input().split()))

cnt = 0


def solve(weight, used):
    global cnt
    if used == (1 << N)-1:
        cnt += 1
        return

    for i in range(N):
        if used & (1 << i):
            continue

        if weight - K + kit[i] >= 500:
            solve(weight - K + kit[i], used | (1 << i))


solve(500, 0)

print(cnt)
