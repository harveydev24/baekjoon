N = int(input())

a = 0


def fib(n):
    global a
    a += 1
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)


print(fib(N), N-2)
