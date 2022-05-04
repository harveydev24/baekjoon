import sys
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
dp_min = [0, 0, 0]
dp_max = [0, 0, 0]

for j in range(3):
    dp_min[j] = lst[-1][j]
    dp_max[j] = lst[-1][j]

for i in range(N-2, -1, -1):
    next_dp_min = [0, 0, 0]
    next_dp_max = [0, 0, 0]
    for j in range(3):
        if j == 0:
            next_dp_min[j] = min(dp_min[j], dp_min[j+1]) + lst[i][j]
            next_dp_max[j] = max(dp_max[j], dp_max[j+1]) + lst[i][j]

        elif j == 1:
            next_dp_min[j] = min(dp_min[j-1], dp_min
                                 [j], dp_min[j+1]) + lst[i][j]
            next_dp_max[j] = max(dp_max[j-1], dp_max
                                 [j], dp_max[j+1]) + lst[i][j]
        elif j == 2:
            next_dp_min[j] = min(dp_min[j], dp_min[j-1]) + lst[i][j]
            next_dp_max[j] = max(dp_max[j], dp_max[j-1]) + lst[i][j]
    dp_min = next_dp_min
    dp_max = next_dp_max

print(max(dp_max), min(dp_min))