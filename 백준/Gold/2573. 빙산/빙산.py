from collections import deque

N, M = map(int, input().split())

arr = []
cnt = 0
year = 0
iceberg = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    for idx, value in enumerate(tmp):
        if value > 0:
            cnt += 1
            iceberg.append([_, idx])
    arr.append(tmp)

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def melt():
    global cnt, year

    melt_lst = {}
    iceberg_cnt = 0
    for r, c in iceberg:
        if arr[r][c] > 0:
            q = deque([[r, c]])
            visited = [[False]*M for _ in range(N)]
            visited[r][c] = True

            while q:
                r, c = q.popleft()
                iceberg_cnt += 1
                melt_cnt = 0
                for i in range(4):
                    rr, cc = r+dr[i], c+dc[i]
                    if 0 <= rr < N and 0 <= cc < M:
                        if not visited[rr][cc] and arr[rr][cc] > 0:
                            visited[rr][cc] = True
                            q.append([rr, cc])
                        elif arr[rr][cc] == 0:
                            melt_cnt += 1
                melt_lst[(r, c)] = melt_cnt
            break

    if iceberg_cnt != cnt:
        print(year)
        exit(0)

    for key, value in melt_lst.items():
        arr[key[0]][key[1]] -= value
        if arr[key[0]][key[1]] <= 0:
            arr[key[0]][key[1]] = 0
            cnt -= 1
    year += 1


while True:
    melt()
    if cnt == 0:
        print(0)
        break
