board = [[0] * 1001 for _ in range(1001)]

N = int(input())
ans = {}
for idx in range(1,N+1):
    x, y, width, height = map(int, input().split())
    ans[idx] = width * height
    for i in range(x, x+width):
        for j in range(y, y+height):
            if board[i][j] != 0:
                ans[board[i][j]] -= 1
                board[i][j] = idx
            else:
                board[i][j] = idx

for i in range(1, N+1):
    print(ans[i])