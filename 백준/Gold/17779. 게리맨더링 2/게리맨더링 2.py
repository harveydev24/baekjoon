N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

whole_sum = sum([sum(x) for x in array])

dr, dc = [1, 1, -1, -1], [1, -1, -1, 1]


def solve():
    global ans

    for r in range(N-2):
        for c in range(1, N-1):
            if 0 <= c-left and c+right < N and r+(left+right) < N:
                result = [0]*5
                boundary = set([(r, c)])
                rr, cc = r, c

                for i in range(4):
                    # right
                    if i == 0 or i == 2:
                        for k in range(right):
                            rr, cc = rr+dr[i], cc+dc[i]
                            boundary.add((rr, cc))
                    # left
                    else:
                        for k in range(left):
                            rr, cc = rr+dr[i], cc+dc[i]
                            boundary.add((rr, cc))

                tmp_sum = 0
                # 1
                for i in range(r+left):
                    for j in range(c+1):
                        if (i, j) in boundary:
                            break
                        result[0] += array[i][j]
                        tmp_sum += array[i][j]
                # 2
                for i in range(r+right+1):
                    for j in range(N-1, c, -1):
                        if (i, j) in boundary:
                            break
                        result[1] += array[i][j]
                        tmp_sum += array[i][j]
                        # 3
                for i in range(r+left, N):
                    for j in range(c+right-left):
                        if (i, j) in boundary:
                            break
                        result[2] += array[i][j]
                        tmp_sum += array[i][j]
                # 4
                for i in range(r+right+1, N):
                    for j in range(N-1, c+right-left-1, -1):
                        if (i, j) in boundary:
                            break
                        result[3] += array[i][j]
                        tmp_sum += array[i][j]
                # 5
                result[4] = whole_sum - tmp_sum
                ans = min(ans, max(result)-min(result))


ans = 10**5
for left in range(1, N-2):
    for right in range(1, N-2):
        solve()

print(ans)
