T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    n = M*N
    if M >= N:
        tmp = x
        while True:
            if ((tmp-1) % N) + 1 == y:
                print(tmp)
                break
            else:
                tmp += M
                if tmp > n:
                    print(-1)
                    break
    else:
        tmp = y
        while True:
            if ((tmp-1) % M) + 1 == x:
                print(tmp)
                break
            else:
                tmp += N
                if tmp > n:
                    print(-1)
                    break
