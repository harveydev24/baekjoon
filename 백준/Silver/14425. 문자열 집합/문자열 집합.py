N, M = map(int, input().split())

S = set([input() for _ in range(N)])
check = [input() for _ in range(M)]

cnt = 0
for word in check:
    if word in S:
        cnt += 1

print(cnt)
