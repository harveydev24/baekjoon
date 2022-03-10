N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = 10**5


def solve(lst, cnt, length):
    global ans

    if N-length < N//2-cnt:
        return

    if length == N:
        if cnt == N//2:
            power = [0, 0]
            for i in range(N):
                for j in range(i+1, N):
                    if lst[i] == lst[j]:
                        power[lst[i]] += (S[i][j]+S[j][i])
            ans = min(ans, abs(power[0]-power[1]))
            return
        else:
            return

    for i in range(2):
        if i == 0:
            solve(lst+[i], cnt, length+1)
        if i == 1 and cnt < N//2:
            solve(lst+[i], cnt+i, length+1)


solve([], 0, 0)
print(ans)
