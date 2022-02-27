N, L = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def check(lst):
    height = lst[0]
    cnt = 1
    for i in range(1, N):
        if height+1<lst[i] or height-1>lst[i]:
            return False
        
        if height == lst[i]:
            cnt += 1
        elif height+1 == lst[i]:
            if cnt>=L:
                height = lst[i]
                cnt = 1
            else:
                return False
        elif height-1 == lst[i]:
            if cnt<0:
                return False
            else:
                height = lst[i]
                cnt = 1-L
    if cnt < 0:
        return False
    else:
        return True

for row in array:
    if check(row):
        ans += 1

array_transposed = zip(*array)

for col in array_transposed:
    if check(col):
        ans += 1

print(ans)