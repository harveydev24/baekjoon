from collections import deque

dr, dc = [1,-1,0,0],[0,0,1,-1]

def rotate_clock(lst):
    return [lst[-1]] + lst[:len(lst)-1]

def rotate_counter_clock(lst):
    return lst[1:] + [lst[0]]

def rotate(lst, d, k):
    if d == 0:
        for _ in range(k):
            lst = rotate_clock(lst)
        return lst
    else:
        for _ in range(k):
            lst = rotate_counter_clock(lst)
        return lst

def bfs(r,c):
    global visited, isRemoved
    q = deque([(r,c)])
    visited[r][c] = True
    remove_lst = [(r,c)]

    while q:
        r,c = q.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if cc == M:
                cc = 0
            elif cc == -1:
                cc = M-1
            if 0<=rr<N and not visited[rr][cc]:
                if plates[r][c] == plates[rr][cc]:
                    q.append((rr,cc))
                    visited[rr][cc] = True
                    remove_lst.append((rr,cc))
    
    if len(remove_lst) >= 2:
        isRemoved = True
        for item in remove_lst:
            plates[item[0]][item[1]] = -1
            



N, M, T = map(int, input().split())
plates = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(N):
        if (i+1)%x == 0:
            plates[i] = rotate(plates[i], d, k)
    
    visited = [[False]*M for _ in range(N)]
    isRemoved = False


    for r in range(N):
        for c in range(M):
            if not visited[r][c] and plates[r][c] != -1:
                bfs(r,c)
    
    if not isRemoved:
        tmp_sum = 0
        cnt = 0
        for r in range(N):
            for c in range(M):
                if plates[r][c] != -1:
                    cnt += 1
                    tmp_sum += plates[r][c]
        if cnt != 0:
            avg = tmp_sum/cnt

            for r in range(N):
                for c in range(M):
                    if plates[r][c] != -1:
                        if plates[r][c] > avg:
                            plates[r][c] -= 1
                        elif plates[r][c] < avg:
                            plates[r][c] += 1

ans = 0
for r in range(N):
    for c in range(M):
        if plates[r][c] != -1:
            ans += plates[r][c]

print(ans)








