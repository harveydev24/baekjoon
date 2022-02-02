
from re import L


N, M, K = map(int, input().split())
ground = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x,y,z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx,dy = [1,-1,0,0,1,-1,-1,1],[0,0,1,-1,1,1,-1,-1]

for _ in range(K):
    #spring and summer
    for i in range(N):
        for j in range(N):
            trees[i][j].sort()
            dead_idx = -1
            for idx, tree_age in enumerate(trees[i][j]):
                if ground[i][j] >= tree_age:
                    ground[i][j] -= tree_age
                    trees[i][j][idx] += 1
                else:
                    dead_idx = idx
                    break
            if dead_idx != -1:
                for tree_age in trees[i][j][dead_idx:]:
                    ground[i][j] += tree_age//2
                trees[i][j] = trees[i][j][:dead_idx]
    #autumn
    for i in range(N):
        for j in range(N):
            for tree_age in trees[i][j]:
                if tree_age%5 == 0:
                    for k in range(8):
                        xx, yy = i+dx[k],j+dy[k]
                        if 0<=xx<N and 0<=yy<N:
                            trees[xx][yy].append(1)
    #winter
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(trees[i][j])
print(cnt)
