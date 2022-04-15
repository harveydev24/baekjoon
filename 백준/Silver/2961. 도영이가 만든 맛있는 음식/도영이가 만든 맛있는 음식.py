N = int(input())
ans = 10**9
soar = []
bit = []
for _ in range(N):
    s, b = map(int, input().split())
    soar.append(s)
    bit.append(b)

for i in range(1 << len(soar)):
    cnt = 0
    s = 1
    b = 0
    for j in range(len(soar)):
        if i & (1 << j):
            cnt += 1
            s *= soar[j]
            b += bit[j]
    if cnt > 0:
        ans = min(ans, abs(s-b))

print(ans)