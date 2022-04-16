n, d = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    num = i

    while num > 0:
        if num % 10 == d:
            cnt += 1
        num //= 10

print(cnt)
