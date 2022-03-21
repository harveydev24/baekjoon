N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
cnt2 = 0
cnt3 = 0


def check(x, y, size):
    for r in range(x, x+size):
        for c in range(y, y+size):
            if array[r][c] != array[x][y]:
                return False
    return True


def solve(x, y, size):
    global cnt, cnt2, cnt3

    if check(x, y, size):
        if array[x][y] == -1:
            cnt += 1
        elif array[x][y] == 0:
            cnt2 += 1
        else:
            cnt3 += 1
    else:
        for i in range(3):
            for j in range(3):
                solve(x+int(size/3)*i, y+int(size/3)*j, int(size/3))


solve(0, 0, N)

print(cnt)
print(cnt2)
print(cnt3)
