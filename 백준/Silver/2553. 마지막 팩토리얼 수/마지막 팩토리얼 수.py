N = int(input())

tmp = 1

for i in range(2, N+1):
    tmp *= i
    while tmp % 10 == 0:
        tmp //= 10
    tmp %= 10000000000

print(tmp % 10)
