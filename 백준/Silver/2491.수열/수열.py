N = int(input())
array = list(map(int, input().split()))

def solve(array):
    if len(array) == 1:
        return 1
    cnt_max = 1
    cnt_tmp = 1
    for i in range(1,N):
        if array[i] >= array[i-1]:
            cnt_tmp += 1
        else:
            cnt_max = max(cnt_max, cnt_tmp)
            cnt_tmp = 1
    cnt_max = max(cnt_max, cnt_tmp)
    cnt_max2 = 1
    cnt_tmp2 = 1
    for i in range(1,N):
        if array[i] <= array[i-1]:
            cnt_tmp2 += 1
        else:
            cnt_max2 = max(cnt_max2, cnt_tmp2)
            cnt_tmp2 = 1
    cnt_max2 = max(cnt_max2, cnt_tmp2)
    return max(cnt_max, cnt_max2)

print(solve(array))