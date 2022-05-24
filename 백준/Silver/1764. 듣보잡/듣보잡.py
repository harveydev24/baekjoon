import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = set()
b = set()
my_set = set()
for _ in range(N):
    name = input().rstrip()
    d.add(name)
    my_set.add(name)

for _ in range(M):
    name = input().rstrip()
    b.add(name)
    my_set.add(name)

ans = []

for name in my_set:
    if name in b and name in d:
        ans.append(name)
print(len(ans))
ans.sort()
for name in ans:
    print(name)
