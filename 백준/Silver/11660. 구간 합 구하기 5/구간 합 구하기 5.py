import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [[0]*(N+1)]
for _ in range(N):
    lst.append([0] + list(map(int, input().split())))

accSum = lst

for r in range(1, N+1):
    for c in range(1, N+1):
        accSum[r][c] = accSum[r-1][c] + accSum[r][c-1] + \
            accSum[r][c] - accSum[r-1][c-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(accSum[x2][y2]-accSum[x2][y1-1]-accSum[x1-1][y2]+accSum[x1-1][y1-1])
