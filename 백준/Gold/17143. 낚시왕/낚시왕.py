def fishing():
    global sharks, ans
    catched = None

    for key, values in sharks.items():
        if key[1] == fisherman:
            if catched == None:
                catched = key
            else:
                if catched[0] > key[0]:
                    catched = key
    if catched != None:
        ans += sharks[catched][2]
        del sharks[catched]


def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


def move():
    global sharks
    next_sharks = {}
    for key, values in sharks.items():
        r, c = key
        s, d, z = values
        for _ in range(s):
            r, c = r+dr[d], c+dc[d]
            if not (0 <= r < R and 0 <= c < C):
                d = change_direction(d)
                r, c = r+dr[d], c+dc[d]
                r, c = r+dr[d], c+dc[d]

        if next_sharks.get((r, c)) == None:
            next_sharks[(r, c)] = (s, d, z)
        else:
            if next_sharks.get((r, c))[2] < z:
                next_sharks[(r, c)] = (s, d, z)

    sharks = next_sharks


R, C, M = map(int, input().split())
sharks = {}


dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = (s, d-1, z)

ans = 0

for fisherman in range(C):
    fishing()
    move()


print(ans)
