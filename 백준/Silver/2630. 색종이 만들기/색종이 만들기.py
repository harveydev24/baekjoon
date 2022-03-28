N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


def check(i, j, size):
    for r in range(i, i+size):
        for c in range(j, j+size):
            if arr[r][c] != arr[i][j]:
                return False
    return True


def solve(i, j, size):
    global blue, white
    if check(i, j, size):
        if arr[i][j]:
            blue += 1
        else:
            white += 1
        return

    for m in range(2):
        for n in range(2):
            solve(i+(size//2)*m, j+(size//2)*n, size//2)


solve(0, 0, N)
print(white)
print(blue)
