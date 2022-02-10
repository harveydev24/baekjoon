N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M+1)//2))
else:
    if M>=7:
        print(M-2)
    else:
        if M<4:
            print(M)
        else:
            print(4)