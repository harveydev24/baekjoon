import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))

X.sort()

lo = 0
hi = 1000000001


def check(mid):
    cnt = 0
    i = 0

    while i < N and X[i] < mid:
        cnt += mid-X[i]
        i += 1

    return cnt <= K


while lo+1 < hi:
    mid = (lo+hi)//2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)
