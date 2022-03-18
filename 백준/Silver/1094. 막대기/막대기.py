X = int(input())
stick = 64
cnt = 0
tmp = 0

while True:
    if tmp + stick > X:
        stick = stick >> 1
    elif tmp + stick <= X:
        cnt += 1
        tmp += stick
        stick = stick >> 1
        if tmp == X:
            print(cnt)
            exit(0)
    

        
    