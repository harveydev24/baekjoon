N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
orders = list(map(int, input().split())) # 1 2 3 4 동 서 북 남

dice = {}
for i in range(1, 7):
    dice[i] = 0

def change():
    global dice, board
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0

def move_north():
    global dice, x, y
    if 0<=x-1<N and 0<=y<M:
        dice[2],dice[1],dice[5],dice[6] = dice[1],dice[5],dice[6],dice[2]
        x, y = x-1, y
        change()
        print(dice[1])

def move_east():
    global dice, x, y
    if 0<=x<N and 0<=y+1<M:
        dice[3],dice[1],dice[4],dice[6] = dice[1],dice[4],dice[6],dice[3]
        x, y = x, y+1
        change()
        print(dice[1])

def move_south():
    global dice, x, y
    if 0<=x+1<N and 0<=y<M:
        dice[2],dice[1],dice[5],dice[6] = dice[6],dice[2],dice[1],dice[5]
        x, y = x+1, y
        change()
        print(dice[1])

def move_west():
    global dice, x, y
    if 0<=x<N and 0<=y-1<M:
        dice[3],dice[1],dice[4],dice[6] = dice[6],dice[3],dice[1],dice[4]
        x, y = x, y-1
        change()
        print(dice[1])

for order in orders:
    if order == 1:
        move_east()
    elif order == 2:
        move_west()
    elif order == 3:
        move_north()
    else:
        move_south()