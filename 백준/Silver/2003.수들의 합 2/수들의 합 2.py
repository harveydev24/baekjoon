N, M = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0,0
tmp_sum = array[0]
cnt = 0

while True:
    if tmp_sum < M:
        end += 1
        if end>=N: break
        tmp_sum += array[end]
    elif tmp_sum == M:
        cnt += 1
        tmp_sum -= array[start]
        start += 1
        end += 1
        if end>=N: break
        tmp_sum += array[end]
    else:
        tmp_sum -= array[start]
        start += 1

print(cnt)