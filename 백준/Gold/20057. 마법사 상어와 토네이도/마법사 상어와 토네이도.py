import time

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
r, c = N//2, N//2
d = 0
out_sum = 0


def front(r, c, d):
    global out_sum, tmp_sum
    rr, cc = r+2*dr[d], c+2*dc[d]
    if 0 <= rr < N and 0 <= cc < N:
        array[rr][cc] += int(0.05*array[r][c])
        tmp_sum += int(0.05*array[r][c])
    else:
        tmp_sum += int(0.05*array[r][c])
        out_sum += int(0.05*array[r][c])

    rr, cc = r+dr[d], c+dc[d]
    if 0 <= rr < N and 0 <= cc < N:
        array[rr][cc] += int(array[r][c]-tmp_sum)
    else:
        out_sum += int(array[r][c]-tmp_sum)
    array[r][c] = 0


def left_right(r, c, d):
    global out_sum, tmp_sum

    front_vec = [dr[d], dc[d]]
    left_vec = [-dc[d], dr[d]]
    right_vec = [dc[d], -dr[d]]

    rr, cc = r+left_vec[0], c+left_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.07*array[r][c])
        array[rr][cc] += int(0.07*array[r][c])
    else:
        tmp_sum += int(0.07*array[r][c])
        out_sum += int(0.07*array[r][c])

    rr, cc = r+2*left_vec[0], c+2*left_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.02*array[r][c])
        array[rr][cc] += int(0.02*array[r][c])
    else:
        tmp_sum += int(0.02*array[r][c])
        out_sum += int(0.02*array[r][c])

    rr, cc = r+right_vec[0], c+right_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.07*array[r][c])
        array[rr][cc] += int(0.07*array[r][c])
    else:
        tmp_sum += int(0.07*array[r][c])
        out_sum += int(0.07*array[r][c])

    rr, cc = r+2*right_vec[0], c+2*right_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.02*array[r][c])
        array[rr][cc] += int(0.02*array[r][c])
    else:
        tmp_sum += int(0.02*array[r][c])
        out_sum += int(0.02*array[r][c])

    rr, cc = r+front_vec[0]+left_vec[0], c+front_vec[1] + left_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.1*array[r][c])
        array[rr][cc] += int(0.1*array[r][c])
    else:
        tmp_sum += int(0.1*array[r][c])
        out_sum += int(0.1*array[r][c])

    rr, cc = r+front_vec[0]+right_vec[0], c+front_vec[1] + right_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.1*array[r][c])
        array[rr][cc] += int(0.1*array[r][c])
    else:
        tmp_sum += int(0.1*array[r][c])
        out_sum += int(0.1*array[r][c])

    rr, cc = r-front_vec[0]+left_vec[0], c-front_vec[1] + left_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.01*array[r][c])
        array[rr][cc] += int(0.01*array[r][c])
    else:
        tmp_sum += int(0.01*array[r][c])
        out_sum += int(0.01*array[r][c])

    rr, cc = r-front_vec[0]+right_vec[0], c-front_vec[1] + right_vec[1]
    if 0 <= rr < N and 0 <= cc < N:
        tmp_sum += int(0.01*array[r][c])
        array[rr][cc] += int(0.01*array[r][c])
    else:
        tmp_sum += int(0.01*array[r][c])
        out_sum += int(0.01*array[r][c])


while r != 0 or c != 0:
    tmp_sum = 0
    visited[r][c] = True
    left_right(r, c, d)
    front(r, c, d)

    if (r != N//2 or c != N//2) and not visited[r-dc[d]][c+dr[d]]:
        r, c = r-dc[d], c+dr[d]
        d = (d+1) % 4
    else:
        r, c = r+dr[d], c+dc[d]

tmp_sum = 0
visited[r][c] = True
left_right(r, c, d)
front(r, c, d)

print(out_sum)
