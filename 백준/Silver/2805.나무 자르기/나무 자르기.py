N, M = map(int, input().split())
array = list(map(int, input().split()))

start = -1
end = max(array)

def check(mid):
    tmp_sum = 0
    for item in array:
        tmp_sum += max(0, item-mid)
    return tmp_sum>=M

while start + 1 < end:
    mid = (start+end)//2

    if check(mid):
        start = mid
    else:
        end = mid

print(start)
