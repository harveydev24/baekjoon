N, M = map(int, input().split())
A = list(map(int, input().split()))

start = -1
end = 10**12 + 1


def check(mid):
    tmp = 0
    for a in A:
        tmp += mid//a

    return tmp < M


while start + 1 < end:
    mid = (start+end)//2
    if check(mid):
        start = mid
    else:
        end = mid

print(end)
