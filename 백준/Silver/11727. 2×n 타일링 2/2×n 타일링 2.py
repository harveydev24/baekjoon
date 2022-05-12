import functools, sys
sys.setrecursionlimit(10**5)

n = int(input())


@functools.lru_cache(None)
def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    return (solve(n-1) + 2*solve(n-2)) % 10007


print(solve(n))
