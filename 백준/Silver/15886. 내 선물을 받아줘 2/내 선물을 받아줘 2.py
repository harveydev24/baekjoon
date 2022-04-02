N = int(input())
lst = list(input())
cnt = 0
start = lst[0]
curr = lst[0]
for d in lst:
    if d == curr:
        continue

    if d != curr and d != start:
        cnt += 1
        curr = d
    elif d != curr and d == start:
        curr = d
        continue
print(cnt)
