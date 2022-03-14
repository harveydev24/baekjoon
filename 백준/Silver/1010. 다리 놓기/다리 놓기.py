
T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    tmp = 1
    for i in range(M, M-N, -1):
        tmp = tmp * i / (M-i+1)

    result.append(int(tmp))

for item in result:
    print(item)