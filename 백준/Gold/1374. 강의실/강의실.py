import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[1])
cnt = 0

q = [lst[0][2]]
cnt = 1

for _, start, end in lst[1:]:
    if start < q[0]:
        cnt += 1
    else:
        heapq.heappop(q)

    heapq.heappush(q, end)


print(cnt)
