N, M, k = map(int, input().split())
array = []
sharks_pos = {}
smell = [[[0, 0] for i in range(N)] for _ in range(N)]
out_sharks = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] > 0:
            sharks_pos[(i, j)] = [tmp[j]]
            smell[i][j] = [tmp[j], k]

sharks = {}
curr_directions = list(map(int, input().split()))

for i in range(M):
    sharks[i+1] = [curr_directions[i], [[]]]

for i in range(M):
    for j in range(4):
        sharks[i+1][1].append(list(map(int, input().split())))

dr, dc = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]


def move():
    global sharks_pos, out_sharks

    next_sharks_pos = {}
    for key, value in sharks_pos.items():
        r, c = key
        d = sharks[value[0]][0]
        empty = False
        tmp_lst = []
        for i in range(4):
            rr, cc = r+dr[sharks[value[0]][1][d][i]], c + \
                dc[sharks[value[0]][1][d][i]]
            if 0 <= rr < N and 0 <= cc < N:
                if smell[rr][cc][0] == 0:
                    if next_sharks_pos.get((rr, cc)) == None:
                        next_sharks_pos[(rr, cc)] = [value[0]]
                        sharks[value[0]][0] = sharks[value[0]][1][d][i]
                    else:
                        next_sharks_pos[(rr, cc)].append(value[0])
                        sharks[value[0]][0] = sharks[value[0]][1][d][i]
                    empty = True
                    break

                if smell[rr][cc][0] == 0 or smell[rr][cc][0] == value[0]:
                    tmp_lst.append(
                        ((rr, cc), sharks[value[0]][1][d][i], value[0]))

        if not empty:
            for item in tmp_lst:
                if next_sharks_pos.get(item[0]) == None:
                    next_sharks_pos[item[0]] = [item[2]]
                    sharks[item[2]][0] = item[1]
                else:
                    next_sharks_pos[item[0]].append([item[2]])
                    sharks[itme[2]][0] = item[1]
                break
    for key, value in next_sharks_pos.items():
        length = len(value)
        if length >= 2:
            next_sharks_pos[key] = [min(value)]
            out_sharks += length-1

    sharks_pos = next_sharks_pos
    for r in range(N):
        for c in range(N):
            if sharks_pos.get((r, c)) == None and smell[r][c][1] > 0:
                smell[r][c][1] -= 1
                if smell[r][c][1] == 0:
                    smell[r][c][0] = 0
            if sharks_pos.get((r, c)) != None:
                shark_num = sharks_pos.get((r, c))[0]
                if smell[r][c][0] == 0:
                    smell[r][c] = [shark_num, k]
                if smell[r][c][0] >= shark_num:
                    smell[r][c] = [shark_num, k]


def check():

    pass


for t in range(1, 1001):
    move()

    if out_sharks == M-1:
        print(t)
        exit(0)
print(-1)
