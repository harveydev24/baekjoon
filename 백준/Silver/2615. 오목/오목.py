from collections import deque

lst = [list(map(int, input().split())) for _ in range(19)]

dr, dc = [1, 0, 1, -1], [0, 1, 1, 1]

for r in range(19):
    for c in range(19):
        if lst[r][c] > 0:
            check = lst[r][c]
            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]
                cnt = 1

                while 0 <= rr < 19 and 0 <= cc < 19 and lst[rr][cc] == check:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= r-dr[i] < 19 and 0 <= c-dc[i] < 19 and lst[r-dr[i]][c-dc[i]] == check:
                            break
                        if 0 <= rr+dr[i] < 19 and 0 <= cc+dc[i] < 19 and lst[rr+dr[i]][cc+dc[i]] == check:
                            break

                        print(check)
                        print(r+1, c+1)
                        exit(0)

                    rr, cc = rr+dr[i], cc+dc[i]

print(0)
