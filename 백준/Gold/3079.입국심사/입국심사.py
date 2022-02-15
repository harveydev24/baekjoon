N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

def check(mid):
    cnt = 0
    for Tk in array:
        cnt += mid//Tk
    return cnt < M

start = 0
end = 10**18+1

while start+1<end:
    mid = (start+end)//2
    if check(mid):
        start = mid
    else:
        end = mid

print(end)