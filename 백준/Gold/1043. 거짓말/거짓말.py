N, M = map(int, input().split())
tmp = list(map(int, input().split()))
true_people = set(tmp[1:])


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x in true_people:
        true_people.add(y)
    if y in true_people:
        true_people.add(x)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


parties = []
parent = [x for x in range(N+1)]
cnt = 0

for _ in range(M):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        union(tmp[i], tmp[i+1])
    parties.append(tmp[1:])

for i in range(N+1):
    find(i)

for party in parties:
    isGo = True
    for item in party:
        if parent[item] in true_people:
            isGo = False
            break

    if isGo:
        cnt += 1

print(cnt)
