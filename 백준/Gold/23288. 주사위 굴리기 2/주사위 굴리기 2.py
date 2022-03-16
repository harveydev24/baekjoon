from collections import deque

dr, dc, = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs():
    global dice_pos
    r, c = dice_pos
    cnt = 1
    q = deque([(r, c)])
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True

    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            rr, cc = curr_r+dr[i], curr_c+dc[i]
            if 0 <= rr < N and 0 <= cc < M:
                if not visited[rr][cc] and arr[rr][cc] == arr[r][c]:
                    cnt += 1
                    q.append((rr, cc))
                    visited[rr][cc] = True

    dp[r][c] = cnt*arr[r][c]

    return dp[r][c]


def move():
    global dice_pos, dice_state, d
    r, c = dice_pos
    rr, cc = r+dr[d], c+dc[d]
    if rr < 0 or rr >= N or cc < 0 or cc >= M:
        d = (d+2) % 4
        rr, cc = r+dr[d], c+dc[d]

    dice_pos = [rr, cc]
    if d == 0:
        dice_state['U'], dice_state['N'], dice_state['D'], dice_state['S'] = dice_state['S'], dice_state['U'], dice_state['N'], dice_state['D']
    elif d == 1:
        dice_state['U'], dice_state['E'], dice_state['D'], dice_state['W'] = dice_state['W'], dice_state['U'], dice_state['E'], dice_state['D']
    elif d == 2:
        dice_state['U'], dice_state['S'], dice_state['D'], dice_state['N'] = dice_state['N'], dice_state['U'], dice_state['S'], dice_state['D']
    elif d == 3:
        dice_state['U'], dice_state['W'], dice_state['D'], dice_state['E'] = dice_state['E'], dice_state['U'], dice_state['W'], dice_state['D']

    if dice_state['D'] > arr[rr][cc]:
        d = (d+1) % 4
    elif dice_state['D'] < arr[rr][cc]:
        d = (d-1) % 4


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dice_pos = [0, 0]
dice_state = {
    'U': 1,
    'D': 6,
    'E': 3,
    'W': 4,
    'N': 2,
    'S': 5
}

d = 1
ans = 0

for _ in range(K):
    move()
    if dp[dice_pos[0]][dice_pos[1]] == 0:
        ans += bfs()
    else:
        ans += dp[dice_pos[0]][dice_pos[1]]

print(ans)
