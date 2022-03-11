import sys
sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(Q):
    idx = [x*(2**L[i]) for x in range(2**N//(2**L[i]))]
    next_array = [[0]*(2**N) for _ in range(2**N)]
    for r in idx:
        for c in idx:
            for rr in range(2**L[i]):
                for cc in range(2**L[i]):
                    next_array[cc+r][2**L[i]-1-rr+c] = array[r+rr][c+cc]

    melting_lst = []

    for r in range(2**N):
        for c in range(2**N):
            cnt = 0
            for k in range(4):
                rr, cc = r+dr[k], c+dc[k]
                if 0 <= rr < 2**N and 0 <= cc < 2**N:
                    if next_array[rr][cc] > 0:
                        cnt += 1
            if cnt <= 2:
                melting_lst.append((r, c))

    for r, c in melting_lst:
        next_array[r][c] -= 1

    array = next_array


def dfs(r, c):
    global tmp_cnt, ice_sum

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0 <= rr < 2**N and 0 <= cc < 2**N:
            if not visited[rr][cc] and array[rr][cc] > 0:
                tmp_cnt += 1
                visited[rr][cc] = True
                ice_sum += array[rr][cc]
                dfs(rr, cc)


ice_sum = 0
cnt = 0
visited = [[False]*(2**N) for _ in range(2**N)]
for r in range(2**N):
    for c in range(2**N):
        if not visited[r][c] and array[r][c] > 0:
            tmp_cnt = 1
            visited[r][c] = True
            ice_sum += array[r][c]
            dfs(r, c)
            cnt = max(cnt, tmp_cnt)

print(ice_sum)
print(cnt)
