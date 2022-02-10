N, M = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0,0
tmp_sum = array[0]
cnt = 0

while True:
    if tmp_sum == M: 
        cnt += 1
        end += 1
        if end>=N: break
        tmp_sum += array[end]
    elif tmp_sum >= M:
        tmp_sum -= array[start]
        start += 1
        if start > end:
            for i in range(start, N):
                if array[i]<=M:
                    start,end = i,i
                    tmp_sum = array[i]
                    break
    else:
        end += 1
        if end>=N: break
        tmp_sum += array[end]

print(cnt)