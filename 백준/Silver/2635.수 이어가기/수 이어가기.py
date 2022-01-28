n = int(input())

cnt_max = 0
ans_lst = []

for i in range(1,n+1):
    cnt = 2
    prev = n
    curr = i
    tmp_lst = [prev, curr]
    while True:
        next = prev - curr

        if next >=0:
            prev = curr
            curr = next
            tmp_lst.append(next)
            cnt += 1
        else:
            if cnt_max < cnt:
                cnt_max = cnt
                ans_lst = tmp_lst
            break
print(cnt_max)
print(' '.join([str(x) for x in ans_lst]))