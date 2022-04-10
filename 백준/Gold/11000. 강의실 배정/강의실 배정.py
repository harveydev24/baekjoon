import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()
cnt = 0

q = [lst[0][1]]
cnt = 1

for start, end in lst[1:]:
    if start < q[0]:
        cnt += 1
    else:
        heapq.heappop(q)

    heapq.heappush(q, end)


print(cnt)
