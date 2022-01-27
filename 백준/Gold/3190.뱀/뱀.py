from collections import deque

N = int(input())
K = int(input())
board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1 # apple
L = int(input())
dir_change_lst = []
for _ in range(L):
    dir_change_lst.append(input().split())

class Snake:
    def __init__(self, dir_change_lst):
        self.curr_pos = deque([(1,1)])
        self.curr_dir = (0,1)
        self.dir_change_lst = deque(dir_change_lst)
        self.cnt = 0
    
    def change_dir(self):
        if self.dir_change_lst:
            if str(self.cnt) == self.dir_change_lst[0][0]:
                if self.dir_change_lst[0][1] == 'L':
                    self.curr_dir = (-self.curr_dir[1], self.curr_dir[0])
                else:
                    self.curr_dir = (self.curr_dir[1], -self.curr_dir[0])
                self.dir_change_lst.popleft()
    
    def game_over_check(self, head):
        if head[0]<1 or head[0]>N or head[1]<1 or head[1]>N:
            print(self.cnt)
            exit(0)
        
        for idx, item in enumerate(self.curr_pos):
            if idx == 0: continue
            if head[0] == item[0] and head[1] == item[1]:
                print(self.cnt)
                exit(0)
    
    def move(self):
        self.cnt += 1
        for idx, item in enumerate(self.curr_pos):
            if idx == 0:
                tmpNext = (self.curr_pos[idx][0]+self.curr_dir[0], self.curr_pos[idx][1]+self.curr_dir[1])
                self.game_over_check(tmpNext)

                if board[tmpNext[0]][tmpNext[1]] == 1:
                    board[tmpNext[0]][tmpNext[1]] = 0
                    self.curr_pos.appendleft(tmpNext)
                    break
                prev = self.curr_pos[idx]
                self.curr_pos[idx] = tmpNext
            else:
                tmp = self.curr_pos[idx]
                self.curr_pos[idx] = prev
                prev = tmp



        self.change_dir() 
    
    def print_board(self):
        tmpboard = [[0] * (N+1) for _ in range(N+1)]
        for item in self.curr_pos:
            tmpboard[item[0]][item[1]] = 5
        for item in tmpboard:
            print(item)

snake = Snake(dir_change_lst)

while True:
    snake.move()
