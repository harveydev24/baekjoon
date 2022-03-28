N = int(input())

lst = [0]*N
B = list(map(int, input().split()))


def check(n):
    plus_cnt, mul_cnt = 0, 0

    while n != 0:
        if n % 2:
            plus_cnt += 1
            n -= 1
        else:
            mul_cnt += 1
            n //= 2

    return plus_cnt, mul_cnt


for i in range(N):
    lst[i] = check(B[i])

ans = 0
max_mul_cnt = 0

for plus_cnt, mul_cnt in lst:
    ans += plus_cnt
    if mul_cnt > max_mul_cnt:
        max_mul_cnt = mul_cnt

ans += max_mul_cnt
print(ans)
