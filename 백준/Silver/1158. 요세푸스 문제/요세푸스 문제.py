from collections import deque
N, K = map(int, input().split())
q = deque(list(range(1, N+1)))
lst = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    lst.append(str(q.popleft()))

print('<'+', '.join(lst)+'>')
