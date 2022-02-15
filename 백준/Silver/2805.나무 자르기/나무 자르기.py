N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for tree in trees:
        sum += max(0, (tree - mid))
    #print('{0} {1} {2} {3}'.format(start, mid, end, sum))
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)