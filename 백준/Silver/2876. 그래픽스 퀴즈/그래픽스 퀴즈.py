N = int(input())
lst = []
dct = {}
for i in range(1, 6):
    dct[i] = 0
for i in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

for i in range(1, 6):
    cnt = 0
    for A, B in lst:
        if A == i or B == i:
            cnt += 1
        else:
            dct[i] = max(dct[i], cnt)
            cnt = 0

    dct[i] = max(dct[i], cnt)
a, b = sorted(list(dct.items()), key=lambda x: (x[1], -x[0]))[-1]
print(b, a)
