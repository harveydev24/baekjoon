from collections import deque

N, M = map(int, input().split())
array = []

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def check(red, blue):
    red_set = set([])
    blue_set = set([])
    for i in range(4):
        rr, cc = red[0] + dr[i], red[1]+dc[i]
        rrr, ccc = blue[0] + dr[i], blue[1]+dc[i]
        if array[rr][cc] == '.' or array[rr][cc] == 'O':
            red_set.add(i)
        if array[rrr][ccc] == '.' or array[rrr][ccc] == 'O':
            blue_set.add(i)

    return red_set | blue_set


for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == 'R':
            red = [i, j]
            tmp[j] = '.'
        elif tmp[j] == 'B':
            blue = [i, j]
            tmp[j] = '.'
        elif tmp[j] == 'O':
            hole = [i, j]
    array.append(tmp)

ans = -1


def move(red_r, red_c, blue_r, blue_c, i, cnt):
    tmp_red_r, tmp_red_c, tmp_blue_r, tmp_blue_c = red_r, red_c, blue_r, blue_c

    while array[tmp_red_r+dr[i]][tmp_red_c+dc[i]] == '.' or array[tmp_red_r+dr[i]][tmp_red_c+dc[i]] == 'O':
        tmp_red_r = tmp_red_r+dr[i]
        tmp_red_c = tmp_red_c+dc[i]
        if array[tmp_red_r][tmp_red_c] == 'O':
            break

    while array[tmp_blue_r+dr[i]][tmp_blue_c+dc[i]] == '.' or array[tmp_blue_r+dr[i]][tmp_blue_c+dc[i]] == 'O':
        tmp_blue_r = tmp_blue_r+dr[i]
        tmp_blue_c = tmp_blue_c+dc[i]
        if array[tmp_blue_r][tmp_blue_c] == 'O':
            break

    if array[tmp_red_r][tmp_red_c] == 'O' and array[tmp_blue_r][tmp_blue_c] == 'O':
        return False

    if array[tmp_red_r][tmp_red_c] == 'O' and array[tmp_blue_r][tmp_blue_c] != 'O':
        print(1)
        exit(0)

    if array[tmp_blue_r][tmp_blue_c] == 'O':
        return False

    if (tmp_red_r, tmp_red_c) == (tmp_blue_r, tmp_blue_c):
        if i == 0:
            if red_r < blue_r:
                tmp_blue_r = tmp_red_r-dr[i]
            else:
                tmp_red_r = tmp_blue_r-dr[i]
        elif i == 1:
            if red_r < blue_r:
                tmp_red_r = tmp_blue_r-dr[i]
            else:
                tmp_blue_r = tmp_red_r-dr[i]

        elif i == 2:
            if red_c < blue_c:
                tmp_blue_c = tmp_red_c-dc[i]
            else:
                tmp_red_c = tmp_blue_c-dc[i]

        elif i == 3:
            if red_c < blue_c:
                tmp_red_c = tmp_blue_c-dc[i]
            else:
                tmp_blue_c = tmp_red_c-dc[i]

    return tmp_red_r, tmp_red_c, tmp_blue_r, tmp_blue_c


def bfs():
    q = deque([(red[0], red[1], blue[0], blue[1], 0)])
    visited = {}
    visited[(red[0], red[1], blue[0], blue[1])] = True

    while q:
        red_r, red_c, blue_r, blue_c, cnt = q.popleft()
        if cnt >= 10:
            break
        direction = check((red_r, red_c), (blue_r, blue_c))

        for i in range(4):
            if i in direction:
                tmp = move(red_r, red_c, blue_r, blue_c, i, cnt)

                if not tmp:
                    continue

                red_r_, red_c_, blue_r_, blue_c_ = tmp

                if visited.get((red_r_, red_c_, blue_r_, blue_c_)) == None:
                    visited[(red_r_, red_c_, blue_r_, blue_c_)] = True
                    q.append((red_r_, red_c_, blue_r_, blue_c_, cnt+1))


bfs()
print(0)
