N = int(input())
my_set = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in my_set:
        print(1, end=' ')
    else:
        print(0, end=' ')
