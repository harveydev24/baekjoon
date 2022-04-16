import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(M):
    k = int(input())
    lst.append(k)

start = 0
end = 10**15


def check(mid):
    cnt = 0
    for item in lst:
        cnt += item//mid
        if item % mid:
            cnt += 1

    return cnt > N


while start+1 < end:
    mid = (start+end)//2

    if check(mid):
        start = mid
    else:
        end = mid

print(end)
