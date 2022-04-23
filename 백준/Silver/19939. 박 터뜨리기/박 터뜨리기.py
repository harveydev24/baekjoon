N, K = map(int, input().split())
tmp = K*(K+1)/2

if tmp > N:
    print(-1)
    exit(0)

N -= tmp

lst = [x for x in range(K+1)]

i = K
while N > 0:
    lst[i] += 1
    i -= 1
    N -= 1
    if i == 0:
        i = K

print(lst[-1]-lst[1])
