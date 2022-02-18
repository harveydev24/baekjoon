N, G, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

start = -1
end = 2*(10**9)+1

def check(mid):
    cnt = 0
    throw_away = []
    for item in array:
        S, L, O = item
        if O == 0:
            cnt += S * max(1, mid-L)
        else:
            throw_away.append(S * max(1, mid-L))
    
    throw_away.sort(reverse=True)
    for i in range(K, len(throw_away)):
        cnt += throw_away[i]
    return cnt<=G

while start+1<end:
    mid = (start+end)//2

    if check(mid):
        start = mid
    else:
        end = mid

print(start)