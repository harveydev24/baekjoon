N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

directions = {0: [-1,0], 1: [0,1], 2: [1,0], 3:[0,-1]}
cnt = 1
area[r][c] = 2
def rotate_dir():
    global d
    d = (d+3)%4

def check_front():
    if area[r+directions[d][0]][c+directions[d][1]] == 0:
        return True
    else:
        return False

def check_back():
    if area[r-directions[d][0]][c-directions[d][1]] == 1:
        return True
    else:
        return False

def move(dr, dc):
    global r, c, area
    r, c = r+dr, c+dc
    area[r][c] = 2

while True:
    is_moved = False
    for _ in range(4):
        rotate_dir()
        if check_front():
            move(directions[d][0], directions[d][1])
            cnt += 1
            is_moved = True
            break
    if not is_moved:
        if check_back():
            print(cnt)
            exit(0)
        else:
            move(-directions[d][0], -directions[d][1])

