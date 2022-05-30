from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
acc_A = [A[0]]

for i in range(1, len(A)):
    acc_A.append(acc_A[-1]+A[i])

acc_A = [0] + acc_A
cnt = defaultdict(int)
for i in range(1, len(acc_A)):
    acc_A[i] %= M
    cnt[acc_A[i]] += 1

ans = 0

for key, value in cnt.items():
    ans += value * (value-1) // 2

print(ans + cnt[0])
