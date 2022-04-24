from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [input().rstrip() for _ in range(N)]
pattern_dct = {}
start_with = set()
patterns = []

for _ in range(K):
    pattern = input().rstrip()
    pattern_dct[pattern] = 0
    tmp = pattern[0]
    start_with.add(tmp)
    for i in range(1, len(pattern)):
        tmp += pattern[i]
        start_with.add(tmp)
    patterns.append(pattern)


dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c, tmp, cnt):
    if tmp in pattern_dct:
        pattern_dct[tmp] += 1

    if cnt == 5:
        return

    for i in range(8):
        rr, cc = (r+dr[i]) % N, (c+dc[i]) % M
        tmp_ = tmp+lst[rr][cc]
        if tmp_ in start_with:
            dfs(rr, cc, tmp_, cnt+1)


for r in range(N):
    for c in range(M):
        if lst[r][c] in start_with:
            dfs(r, c, lst[r][c], 1)


for pattern in patterns:
    print(pattern_dct[pattern])
