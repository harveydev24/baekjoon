import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

for _ in range(M):
    B.append(list(map(int, input().split())))


for i in range(N):
    for k in range(K):
        tmp = 0
        for j in range(M):
            tmp += A[i][j]*B[j][k]
        print(tmp, end=' ')
    print()
