
N, M = map(int, input().split())
board = []
for _ in range(N):
    row = [int(x) for x in input().split()]
    board.append(row)

def rotate_polinomino_clockwise(dir):
    tmp = []
    for item in dir:
        tmp.append((-item[1], item[0]))
    return tmp 

def flip_polinomino(dir):
    tmp = []
    for item in dir:
        tmp.append((item[0], -item[1]))
    return tmp

def sum_process(x, y, dir):
    tmp_sum = 0
    for item in dir:
        xx, yy = x + item[0], y + item[1]
        if 0<=xx<N and 0<=yy<M:
            tmp_sum += board[xx][yy]
        else:
            return 0
    return tmp_sum


def sum_polinominos(x, y, dir):
    tmp_max = 0
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = flip_polinomino(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))
    dir = rotate_polinomino_clockwise(dir)
    tmp_max = max(tmp_max, sum_process(x, y, dir))

    return tmp_max

def solve():
    polinominos = [[(0,0), (0,1), (0,2), (0,3)],
        [(0,0), (1,0), (0,1), (1,1)],
        [(0,0), (1,0), (2,0), (2,1)],
        [(0,0), (1,0), (1,1), (2,1)],
        [(0,0), (0,1), (0,2), (1,1)]]
    
    tmp_max = 0
    for polinomino in polinominos:
        for i in range(N):
            for j in range(M):
                tmp_max = max(tmp_max, sum_polinominos(i, j, polinomino))
    print(tmp_max)

solve()