N = int(input())
array = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for item in array:
    cnt += 1
    item = item - B
    if item > 0:
        cnt += item//C
        if item%C != 0:
            cnt += 1

print(cnt)