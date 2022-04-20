n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
length = sum(a)
ans = 0

for i in range(len(a)-1):
    length -= a[i]
    ans += a[i]*length

print(ans)
