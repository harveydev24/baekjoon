N, r, c = map(int, input().split())


def solve(r, c, size):
    if size == 1:
        return 0

    size = size//2

    if r < size:
        if c < size:
            return solve(r, c, size)
        else:
            return solve(r, c-size, size) + size**2

    else:
        if c < size:
            return solve(r-size, c, size) + 2*(size**2)

        else:
            return solve(r-size, c-size, size) + 3*(size**2)


print(solve(r, c, 2**N))
