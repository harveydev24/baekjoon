# 입력 받기 및 배열 정렬
N, C = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()

# 이분 탐색 조건 함수
def check(mid):
    cnt = 1
    tmp_dist = 0
    for i in range(len(array)-1):
        tmp_dist += array[i+1]-array[i]
        if tmp_dist >= mid:
            tmp_dist = 0
            cnt += 1
    return cnt >= C

# 시작/도착점 설정
start = 0
end = array[-1]-array[0]+1

# 이분탐색 수행
while start + 1 < end:
    mid = (start+end)//2

    if check(mid):
        start = mid
    else:
        end = mid

print(start)