board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
num = []
for _ in range(5):
    num.extend(list(map(int, input().split())))

cnt = 0

for i in range(len(num)):
    for row in range(5):
        for col in range(5):
            if board[row][col] == num[i]:
                board[row][col] = 0

                for j in range(1, 5): # 가로
                    if board[row][j-1] == board[row][j]:
                        if j == 4:
                            cnt += 1
                            if cnt == 3:
                                print(i+1)
                                exit(0)
                    else: break

                for k in range(1, 5): # 세로
                    if board[k-1][col] == board[k][col]:
                        if k == 4:
                            cnt += 1
                            if cnt == 3:
                                print(i+1)
                                exit(0)
                    else: break
                
                if row + col == 4:
                    for l in range(1, 5): # 우상향 대각선
                        if board[l-1][5-l] == board[l][4-l]:
                            if l == 4:
                                cnt += 1
                                if cnt == 3:
                                    print(i+1)
                                    exit(0)
                        else: break

                if row == col:
                    for m in range(1, 5): # 우하향 대각선
                        if board[m-1][m-1] == board[m][m]:
                            if m == 4:
                                cnt += 1
                                if cnt == 3:
                                    print(i+1)
                                    exit(0)
                        else: break
                break
    
