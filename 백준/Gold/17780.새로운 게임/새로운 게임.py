N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
chess_board = [[[] for _ in range(N)] for _ in range(N)]
dr, dc = [0,0,-1,1],[1,-1,0,0]
chess_pieces = [[-1,-1,-1] for _ in range(K+1)] # r, c, d

for i in range(1, K+1):
    r, c, d = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    chess_pieces[i][0], chess_pieces[i][1], chess_pieces[i][2] = r, c, d
    chess_board[r][c].append(i)

def move(i):
    global chess_board, isMoved
    r, c, d = chess_pieces[i][0],chess_pieces[i][1],chess_pieces[i][2]
    rr, cc = r+dr[d], c+dc[d]
    idx = chess_board[r][c].index(i)
    stay = chess_board[r][c][:idx]
    leave = chess_board[r][c][idx:]
    # blue
    if rr<0 or rr>=N or cc<0 or cc>=N or array[rr][cc] == 2:
        pass
    #white
    elif array[rr][cc] == 0:
        isMoved = True
        chess_board[r][c] = stay
        chess_board[rr][cc].extend(leave)
        for i in leave:
            chess_pieces[i][0],chess_pieces[i][1] = rr, cc
        if len(chess_board[rr][cc])>=4:
            print(cnt)
            exit(0)
    # red
    elif array[rr][cc] == 1:
        isMoved = True
        chess_board[r][c] = stay
        chess_board[rr][cc].extend(leave[::-1])
        for i in leave:
            chess_pieces[i][0],chess_pieces[i][1] = rr, cc
        if len(chess_board[rr][cc])>=4:
            print(cnt)
            exit(0)

def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

cnt = 0
while True:
    cnt += 1
    isMoved = False
    for i in range(1, K+1):
        r, c, d = chess_pieces[i][0], chess_pieces[i][1], chess_pieces[i][2]
        rr, cc = r+dr[d], c+dc[d]
        # blue
        if chess_board[r][c][0] == i:
            if rr<0 or rr>=N or cc<0 or cc>=N or array[rr][cc] == 2:
                chess_pieces[i][2] = change_direction(chess_pieces[i][2])
                move(i)
            # white and red
            else:
                move(i)

    if not isMoved or cnt>1000:
        print(-1)
        exit(0)






