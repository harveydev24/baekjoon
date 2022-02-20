from math import gcd
N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()
interval = []



for i in range(1, len(array)):
    interval.append(array[i]-array[i-1])
ans = []

tmp = interval[0]
for i in range(1, len(interval)):
    tmp = gcd(tmp, interval[i])

for i in range(2, tmp+1):
    if tmp%i == 0:
        ans.append(i)

print(' '.join([str(x) for x in ans]))


