N, M = map(int, input().split())

possible = []
DONE = (1 << N) - 1


for _ in range(M):
    lst = list(map(int, input().split()))
    tmp = 0
    for i in range(1, lst[0]+1):
        tmp += (1 << (lst[i]-1))
    possible.append(tmp)

ans = 10**3

for i in range(1 << M):
    tmp = 0
    cnt = 0
    for j in range(M):
        if i & (1 << j):
            tmp = tmp | possible[j]
            cnt += 1

    if tmp == DONE:
        ans = min(ans, cnt)

if ans == 10**3:
    print(-1)
else:
    print(ans)