width, heigth = map(int, input().split())
N = int(input())
l = (width + heigth) * 2 # 영역 둘레
shop_lst = [] # 마지막은 동근이 위치

ans = 0

for _ in range(N+1):
    dir, coor = map(int, input().split())
    if dir == 1: # 북
        shop_lst.append((width-coor) + width + heigth)
    elif dir == 2: # 남
        shop_lst.append(coor)
    elif dir == 3: # 서
        shop_lst.append(2*width + heigth + coor)
    else: # 동
        shop_lst.append(width + heigth - coor)

for i in range(N):
    if shop_lst[i] >= shop_lst[-1]:
        clock = (shop_lst[i] - shop_lst[-1])
        counter_clock = l - clock
    else:
        clock =l - (shop_lst[-1] - shop_lst[i])
        counter_clock = shop_lst[-1] - shop_lst[i]
    ans += min(clock, counter_clock)

print(ans)