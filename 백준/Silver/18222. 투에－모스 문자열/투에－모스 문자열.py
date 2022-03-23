import sys
sys.setrecursionlimit(10**5)

k = int(input())

i = 0
while True:
    if (2**i) >= k:
        break
    i += 1
i -= 1


def solve(k, i, cnt):
    if k == 1:
        if cnt % 2:
            print(1)
        else:
            print(0)
        return

    k = k-2**i
    i = 0
    while True:
        if (2**i) >= k:
            break
        i += 1
    i -= 1

    solve(k, i, cnt+1)


solve(k, i, 0)
