import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

lst = []
parent = [x for x in range(N+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[max(x, y)] = min(x, y)


for _ in range(M):
    a, b, c = map(int, input().split())
    if a != b:
        lst.append((c, a, b))

lst.sort()
cnt = 1
ans = 0
for c, a, b in lst:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += c
    if cnt == N:
        break

print(ans)
