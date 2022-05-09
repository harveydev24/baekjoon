import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    answer = []
    max_heap = []
    min_heap = []
    dct = defaultdict(int)

    for i in range(N):
        operation = input()
        order, n = operation.split()
        n = int(n)

        if order == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            dct[n] += 1
        else:
            if n == 1:
                while max_heap and dct[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    out = heapq.heappop(max_heap)
                    dct[-out] -= 1

            else:
                while min_heap and dct[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    out = heapq.heappop(min_heap)
                    dct[out] -= 1

    while max_heap and dct[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and dct[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])
