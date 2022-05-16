import sys
input = sys.stdin.readline
N, S = map(int, input().split())
cnt = 0

cows = [int(input()) for _ in range(N)]
cows.sort()

for i in range(N-1):
    for j in range(i+1, N):
        if cows[i] + cows[j] <= S:
            cnt += 1
        else:
            break

print(cnt)