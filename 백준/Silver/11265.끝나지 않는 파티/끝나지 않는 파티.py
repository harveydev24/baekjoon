import sys
input = sys.stdin.readline
N, M = map(int, input().split())

costs = [[float('inf')]*N for _ in range(N)]

for i in range(N):
    cost = list(map(int, input().split()))
    for j in range(N):
        costs[i][j] = cost[j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])

for _ in range(M):
    A, B, C = map(int, input().split())
    if costs[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")

