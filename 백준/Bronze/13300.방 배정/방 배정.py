import math
N, K = map(int, input().split())

students = {}
for i in range(1, 7):
    students[i] = [0, 0]

for _ in range(N):
    S, Y = map(int, input().split())
    students[Y][S] += 1

cnt = 0

for i in range(1,7):
    for item in students[i]:
        cnt += math.ceil((item/K))

print(cnt)