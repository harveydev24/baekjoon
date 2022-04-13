try:
    while True:
        N, M = map(int, input().split())
        cnt = 0

        for i in range(N, M+1):
            lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            num = i
            check = True
            while num > 0:
                num, mod = divmod(num, 10)
                if lst[mod] == 1:
                    check = False
                    break
                lst[mod] += 1
            if check:
                cnt += 1

        print(cnt)

except:
    pass