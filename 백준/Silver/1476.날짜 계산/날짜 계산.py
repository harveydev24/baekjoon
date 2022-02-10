E, S, M = map(int, input().split())

tmp = [1,1,1]
cnt = 1
while True:
    if tmp[0]==16: tmp[0]=1
    if tmp[1]==29: tmp[1]=1
    if tmp[2]==20: tmp[2]=1

    if (tmp[0],tmp[1],tmp[2]) == (E,S,M):
        print(cnt)
        exit(0)
    cnt += 1
    tmp[0],tmp[1],tmp[2] = tmp[0]+1,tmp[1]+1,tmp[2]+1
    
