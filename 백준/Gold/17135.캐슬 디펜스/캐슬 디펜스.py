from collections import deque
from itertools import combinations
import copy

N,M,D = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
tmp = [x for x in range(M)]
bow_pos_comb = list(combinations(tmp, 3))
ans = 0
for bow_pos in bow_pos_comb:
    castle = [0]*M
    for pos in bow_pos:
        castle[pos] = 2
    array_ = copy.deepcopy(array)
    array_.append(castle)
    cnt = 0

    def move():
        global array_
        array_ = [[0]*M] + array_[:N-1] + [castle]

    def findTarget(bow_pos):
        target_lst1 = []
        target_lst2 = []
        target_lst3 = []
        target_lst = []
        dist_min1 = float('inf')
        dist_min2 = float('inf')
        dist_min3 = float('inf')
        for i in range(N,-1,-1):
            for j in range(M):
                if array_[i][j] == 1:
                    dist1 = abs(N-i)+abs(bow_pos[0]-j)
                    dist2 = abs(N-i)+abs(bow_pos[1]-j)
                    dist3 = abs(N-i)+abs(bow_pos[2]-j)
                    if dist1==dist_min1 and dist1<=D:
                        target_lst1.append((i,j))
                    if dist1<dist_min1 and dist1<=D:
                        dist_min1 = dist1
                        target_lst1.clear()
                        target_lst1.append((i,j))
                    if dist2==dist_min2 and dist2<=D:
                        target_lst2.append((i,j))
                    if dist2<dist_min2 and dist2<=D:
                        dist_min2 = dist2
                        target_lst2.clear()
                        target_lst2.append((i,j))
                    if dist3==dist_min3 and dist3<=D:
                        target_lst3.append((i,j))
                    if dist3<dist_min3 and dist3<=D:
                        dist_min3 = dist3
                        target_lst3.clear()
                        target_lst3.append((i,j))
        target_lst1.sort(key=lambda x: x[1])
        target_lst2.sort(key=lambda x: x[1])
        target_lst3.sort(key=lambda x: x[1])
        if target_lst1: target_lst.append(target_lst1[0])
        if target_lst2: target_lst.append(target_lst2[0])
        if target_lst3: target_lst.append(target_lst3[0])
        return target_lst
        

    
    for _ in range(N):
        target_lst = findTarget(bow_pos)
        for target in target_lst:
            if array_[target[0]][target[1]] == 1:
                array_[target[0]][target[1]] = 0
                cnt += 1
        move()
    ans = max(ans, cnt)
print(ans)

