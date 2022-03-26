import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []
heapq.heapify(heap)
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(heap, (start, end))

user = [0] * N
computers = [0] * N

cnt = 0

while heap:
    start, end = heapq.heappop(heap)
    for i in range(N):
        if computers[i] <= start:
            if computers[i] == 0:
                cnt += 1
            computers[i] = end
            user[i] += 1
            break

print(cnt)
for i in range(cnt):
    print(user[i], end=" ")
