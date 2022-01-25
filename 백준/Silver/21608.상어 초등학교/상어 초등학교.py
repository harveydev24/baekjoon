N = int(input())
classRoom = [[0] * N for _ in range(N)]
likelst = [[] for _ in range(N**2+1)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def findSeat(likelst):
    tmpLikeMax = 0
    tmpCntMax = 0
    candidateLst = []
    ck = 0
    for x in range(N):
        for y in range(N):
            if classRoom[x][y] != 0: continue
            tmpLike = 0
            emptyCnt = 0
            for k in range(4):
                xx, yy = x + dx[k], y + dy[k]
                if 0<=xx<N and 0<=yy<N:
                    if classRoom[xx][yy] == 0:
                        emptyCnt += 1
                    if classRoom[xx][yy] in likelst:
                        tmpLike += 1
            if tmpLike > tmpLikeMax:
                candidateLst.clear()
                candidateLst.append((x,y))
                tmpLikeMax = tmpLike
                tmpCntMax = emptyCnt
            elif tmpLike == tmpLikeMax:
                if emptyCnt > tmpCntMax:
                    candidateLst.clear()
                    candidateLst.append((x, y))
                    tmpLikeMax = tmpLike
                    tmpCntMax = emptyCnt
                elif emptyCnt == tmpCntMax:
                    candidateLst.append((x, y))
                    tmpLikeMax = tmpLike
                    tmpCntMax = emptyCnt

    return candidateLst[0]
ck = 0          
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    if ck == 0:
        classRoom[1][1] = a
        likelst[a] += [b, c, d, e]
        ck = 1
        continue
    likelst[a] += [b, c, d, e]
    x, y = findSeat([b, c, d, e])
    classRoom[x][y] = a


ans = 0

for x in range(N):
    for y in range(N):
        tmpCnt = 0
        for k in range(4):
            xx, yy = x + dx[k], y + dy[k]
            if 0<=xx<N and 0<=yy<N:
                if classRoom[xx][yy] in likelst[classRoom[x][y]]:
                    tmpCnt += 1
        if tmpCnt == 0:
            ans += 0
        elif tmpCnt == 1:
            ans += 1
        elif tmpCnt == 2:
            ans += 10
        elif tmpCnt == 3:
            ans += 100
        else:
            ans += 1000

print(ans)
