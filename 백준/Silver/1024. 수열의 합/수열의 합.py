N, L = map(int, input().split())


for i in range(L, 101):
    x = N-(i*(i+1)//2)

    if x % i == 0:
        x = x//i

        if x >= -1:
            for j in range(1, i+1):
                print(x+j, end=' ')
            exit(0)
print(-1)