d, n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.append(d)
array.sort()
start = 0
end = d+1

def check(mid):
    # 버리는 돌
    cnt = 0
    # 현재 위치
    curr_pos = 0
    for stone in array:
        if stone-curr_pos < mid:
            cnt += 1
        else:
            curr_pos = stone
    return cnt <= m
    

while start+1<end:
    mid = (start+end)//2
    if check(mid):
        start = mid
    else:
        end = mid

print(start)
