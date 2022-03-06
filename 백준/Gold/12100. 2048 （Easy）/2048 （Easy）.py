import copy

N = int(input())


def up(array):
    for c in range(N):

        tmp = []
        tmp2 = []
        for r in range(N):
            if array[r][c] != 0:
                tmp.append(array[r][c])

        while len(tmp) < N:
            tmp.append(0)

        r = 0
        while r < N-1:
            if tmp[r] == tmp[r+1]:
                tmp[r] = 2*tmp[r]
                tmp[r+1] = 0
            r += 1

        for r in range(N):
            if tmp[r] != 0:
                tmp2.append(tmp[r])

        while len(tmp2) < N:
            tmp2.append(0)

        for r in range(N):
            array[r][c] = tmp2[r]


def down(array):
    for c in range(N):

        tmp = []
        tmp2 = []
        for r in range(N-1, -1, -1):
            if array[r][c] != 0:
                tmp.append(array[r][c])

        while len(tmp) < N:
            tmp.append(0)

        r = 0
        while r < N-1:
            if tmp[r] == tmp[r+1]:
                tmp[r] = 2*tmp[r]
                tmp[r+1] = 0
            r += 1

        for r in range(N):
            if tmp[r] != 0:
                tmp2.append(tmp[r])

        while len(tmp2) < N:
            tmp2.append(0)

        for r in range(N-1, -1, -1):
            array[r][c] = tmp2[N-1-r]


def left(array):
    for r in range(N):

        tmp = []
        tmp2 = []

        for c in range(N):
            if array[r][c] != 0:
                tmp.append(array[r][c])

        while len(tmp) < N:
            tmp.append(0)

        c = 0
        while c < N-1:
            if tmp[c] == tmp[c+1]:
                tmp[c] = 2*tmp[c]
                tmp[c+1] = 0
            c += 1

        for c in range(N):
            if tmp[c] != 0:
                tmp2.append(tmp[c])

        while len(tmp2) < N:
            tmp2.append(0)

        for c in range(N):
            array[r][c] = tmp2[c]


def right(array):
    for r in range(N):

        tmp = []
        tmp2 = []

        for c in range(N-1, -1, -1):
            if array[r][c] != 0:
                tmp.append(array[r][c])

        while len(tmp) < N:
            tmp.append(0)

        c = 0
        while c < N-1:
            if tmp[c] == tmp[c+1]:
                tmp[c] = 2*tmp[c]
                tmp[c+1] = 0
            c += 1

        for c in range(N):
            if tmp[c] != 0:
                tmp2.append(tmp[c])

        while len(tmp2) < N:
            tmp2.append(0)

        for c in range(N-1, -1, -1):
            array[r][c] = tmp2[N-1-c]


array = [list(map(int, input().split())) for _ in range(N)]


def solve(array, cnt):
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, array)))
        return

    for i in range(4):
        if i == 0:
            tmp = [row[:] for row in array]
            up(array)
            solve(array, cnt + 1)
            array = tmp
        elif i == 1:
            tmp = [row[:] for row in array]
            down(array)
            solve(array, cnt + 1)
            array = tmp

        elif i == 2:
            tmp = [row[:] for row in array]
            left(array)
            solve(array, cnt + 1)
            array = tmp

        elif i == 3:
            tmp = [row[:] for row in array]
            right(array)
            solve(array, cnt + 1)
            array = tmp


ans = 2

solve(array, 0)
print(ans)
