import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
acc = []
for item in lst:
    if not acc:
        acc.append(item)
    else:
        acc.append(acc[-1]+item)

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if i == 0:
        print(acc[j])
    else:
        print(acc[j]-acc[i-1])
