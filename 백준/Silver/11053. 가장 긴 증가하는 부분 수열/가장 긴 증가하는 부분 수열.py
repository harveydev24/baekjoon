N = int(input())
A = list(map(int, input().split()))
ans = [1] * len(A)

for i in range(1,len(A)):
    for j in range(i):
        if A[i] > A[j]: ans[i] = max(ans[i], ans[j] + 1)

print(max(ans))