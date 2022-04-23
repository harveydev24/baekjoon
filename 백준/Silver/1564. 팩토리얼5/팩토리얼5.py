N = int(input())

tmp = 1

for i in range(2, N+1):
    tmp *= i
    while tmp % 10 == 0:
        tmp //= 10
    tmp %= 1000000000000000

print(str(tmp % 100000).zfill(5))
