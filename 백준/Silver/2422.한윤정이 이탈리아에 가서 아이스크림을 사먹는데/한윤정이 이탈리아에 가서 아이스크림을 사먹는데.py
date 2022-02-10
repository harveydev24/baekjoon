N, M = map(int,input().split())
relation = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

cnt = 0

for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if j not in relation[i] and k not in relation[i] and k not in relation[j]:
                cnt += 1

print(cnt)