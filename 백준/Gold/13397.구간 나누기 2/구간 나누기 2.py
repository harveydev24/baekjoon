N, M = map(int, input().split())
array = list(map(int, input().split()))

start = -1
end = max(array) - min(array) + 1

# 구간 점수의 최댓값이 mid일때,
# 만들 수 있는 구간 개수의 최솟값
def check(mid):
    cnt = 1
    tmp_max = 0
    tmp_min = 10001
    tmp = []
    for n in array:
        tmp_max = max(tmp_max, n)
        tmp_min = min(tmp_min, n)
        if tmp_max - tmp_min > mid:
            cnt += 1
            tmp_max = n
            tmp_min = n
    return cnt > M

while start+1<end:
    mid = (start+end)//2
    if check(mid):
        start = mid
    else:
        end = mid
print(end)