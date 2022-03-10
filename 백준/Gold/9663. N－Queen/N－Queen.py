N = int(input())


board = [0] * N
cnt = 0

def isPossible(i):
    for k in range(i):
        if board[k] == board[i]: return False
        if abs(k-i) == abs(board[k]-board[i]): return False
    return True

def DFS(i):
    global cnt
    if i == N:
        cnt += 1
        return
    else:
        for j in range(N):
            board[i] = j
            if isPossible(i):
                DFS(i+1)

DFS(0)
print(cnt)
            

