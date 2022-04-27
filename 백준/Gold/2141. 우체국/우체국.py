N = int(input())
A = dict()
X = []
total_A = 0

for _ in range(N):
    x, a = map(int, input().split())
    X.append(x)
    A[x] = a
    total_A += a

if total_A % 2:
    total_A += 1

X.sort()

tmp_sum = 0
for x in X:
    tmp_sum += A[x]
    if tmp_sum >= total_A//2:
        print(x)
        break