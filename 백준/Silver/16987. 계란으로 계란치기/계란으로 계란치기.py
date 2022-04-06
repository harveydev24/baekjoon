N = int(input())
eggs = []
ans = 0


def solve(idx, cnt):
    global ans
    if idx == N or cnt == N-1:
        ans = max(ans, cnt)
        return

    if eggs[idx][0] <= 0:
        solve(idx+1, cnt)
        return

    for i in range(N):
        if i == idx:
            continue

        if eggs[i][0] > 0:
            eggs[i][0] -= eggs[idx][1]
            eggs[idx][0] -= eggs[i][1]
            if eggs[i][0] <= 0 and eggs[idx][0] <= 0:
                solve(idx+1, cnt+2)
            elif eggs[i][0] <= 0 or eggs[idx][0] <= 0:
                solve(idx+1, cnt+1)
            else:
                solve(idx+1, cnt)
            eggs[i][0] += eggs[idx][1]
            eggs[idx][0] += eggs[i][1]
        # else:
        #     solve(idx + 1, cnt)


for _ in range(N):
    S, W = map(int, input().split())
    eggs.append([S, W])

solve(0, 0)

print(ans)
