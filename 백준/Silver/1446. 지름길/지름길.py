import heapq

N, D = map(int, input().split())
nodes = [0]
edges = []

for _ in range(N):
    start, end, dist = map(int, input().split())
    if end > D:
        continue
    edges.append((start, end, dist))
    nodes.extend([start, end])
if D not in nodes:
    nodes.append(D)
nodes.sort()
adj = {}

for i in range(len(nodes)):
    if i == len(nodes)-1:
        adj[nodes[i]] = []
        break
    adj[nodes[i]] = [(nodes[i+1], nodes[i+1]-nodes[i])]

for start, end, dist in edges:
    adj[start].append((end, dist))


def dijkstra(n):
    distances = {}
    for key in adj.keys():
        distances[key] = float('inf')

    distances[0] = 0
    q = [(0, 0)]  # dist, node
    heapq.heapify(q)

    while q:
        dist, node = heapq.heappop(q)
        if dist > distances[node]:
            continue

        for next in adj[node]:
            if dist + next[1] < distances[next[0]]:
                distances[next[0]] = dist + next[1]
                q.append((distances[next[0]], next[0]))

    print(distances[D])


dijkstra(0)
