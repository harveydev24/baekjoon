import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    row_sum = []
    col_sum = []
    for r in range(N):
        tmp = 0
        for c in range(N):
            tmp += lst[r][c]
        row_sum.append(tmp)
    for c in range(N):
        tmp = 0
        for r in range(N):
            tmp += lst[r][c]
        col_sum.append(tmp)

    for i in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for r in range(r1-1, r2):
            row_sum[r] += v*(abs(c1-c2)+1)
        for c in range(c1-1, c2):
            col_sum[c] += v*(abs(r1-r2)+1)

    print(*row_sum)
    print(*col_sum)
