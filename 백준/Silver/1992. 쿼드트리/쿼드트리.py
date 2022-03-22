import sys
sys.setrecursionlimit(10**5)
N = int(input())

arr = [list(input()) for _ in range(N)]


def check(r, c, N):
    for i in range(r, r+N):
        for j in range(c, c+N):
            if arr[i][j] != arr[r][c]:
                return False
    return True


def quad_tree(r, c, N):
    if check(r, c, N):
        return arr[r][c]
    else:
        tmp = '('
        for i in range(2):
            for j in range(2):
                tmp += quad_tree(r+int(N/2)*i, c+int(N/2)*j, int(N/2))
        return tmp + ')'


print(quad_tree(0, 0, N))
