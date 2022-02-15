N, M, L = map(int, input().split())
array = list(map(int, input().split()))
array.extend([0, L])
array.sort()

start = 1
end = L-1
ans = 0
while start<=end:
    mid = (start+end)//2
    cnt = 0

    for i in range(len(array)-1):
        dist = array[i+1]-array[i]
        if dist>mid:
            cnt += (dist-1)//mid
    if cnt>M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)
