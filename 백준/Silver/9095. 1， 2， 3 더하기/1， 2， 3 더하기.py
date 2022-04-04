T = int(input())

lst = [0] * 12
lst[1] = 1
lst[2] = 2
lst[3] = 4
for i in range(4, 12):
    lst[i] = lst[i-1] + lst[i-2] + lst[i-3]

for _ in range(T):
    n = int(input())
    print(lst[n])
