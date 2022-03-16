from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(r, c, block_num, visited):
    q = deque([(r, c)])
    color = arr[r][c]
    tmp = {
        'members': [(r, c)],
        'rainbow': 0,
        'row': r,
        'col': c,
        'size': 1
    }
    rainbows = []

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < N and 0 <= cc < N:
                if not visited[rr][cc]:
                    if arr[rr][cc] == 0 or arr[rr][cc] == color:
                        visited[rr][cc] = True
                        tmp['members'].append((rr, cc))
                        q.append((rr, cc))
                        tmp['size'] += 1
                        if arr[rr][cc] == 0:
                            tmp['rainbow'] += 1
                            rainbows.append((rr, cc))
                        if arr[rr][cc] == color:
                            if tmp['row'] > rr:
                                tmp['row'] = rr
                                tmp['col'] = cc
                            if tmp['row'] == rr:
                                if tmp['col'] > cc:
                                    tmp['row'] = rr
                                    tmp['col'] = cc
    for r, c, in rainbows:
        visited[r][c] = False

    if tmp['size'] > 1:
        block_state[block_num] = tmp
        return block_num + 1
    else:
        return block_num


def find_block():
    visited = [[False]*N for _ in range(N)]
    block_num = 1

    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > 0:
                visited[r][c] = True
                block_num = bfs(r, c, block_num, visited)


def gravity():
    global arr
    tmp_arr = [[-2]*N for _ in range(N)]
    for c in range(N):
        idx = N-1
        tmp = []
        for r in range(N-1, -1, -1):
            if arr[r][c] >= 0:
                tmp.append(arr[r][c])
            if arr[r][c] == -1:
                tmp_arr[r][c] = -1
                for i in range(len(tmp)):
                    tmp_arr[idx-i][c] = tmp[i]
                idx = r-1
                tmp = []

        for i in range(len(tmp)):
            tmp_arr[idx-i][c] = tmp[i]

    arr = [x[:] for x in tmp_arr]


def rotation():
    global arr
    rotated_arr = [x[:] for x in arr]
    for r in range(N):
        for c in range(N):
            rotated_arr[r][c] = arr[c][N-1-r]
    arr = [x[:] for x in rotated_arr]


ans = 0

while True:
    block_state = {}
    find_block()
    if block_state == {}:
        break

    tmp_key = 1
    for key, value in block_state.items():
        if value['size'] > block_state[tmp_key]['size']:
            tmp_key = key
        elif value['size'] == block_state[tmp_key]['size']:
            if value['rainbow'] > block_state[tmp_key]['rainbow']:
                tmp_key = key
            elif value['rainbow'] == block_state[tmp_key]['rainbow']:
                if value['row'] > block_state[tmp_key]['row']:
                    tmp_key = key
                elif value['row'] == block_state[tmp_key]['row']:
                    if value['col'] > block_state[tmp_key]['col']:
                        tmp_key = key

    for r, c in block_state[tmp_key]['members']:
        arr[r][c] = -2

    ans += block_state[tmp_key]['size']**2
    gravity()
    rotation()
    gravity()

print(ans)
