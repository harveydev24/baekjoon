N, M = map(int, input().split())

trains = [0]*(N+1)

for _ in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        trains[tmp[1]] = (trains[tmp[1]] | (1 << (tmp[2]-1)))
    elif tmp[0] == 2:
        trains[tmp[1]] = (trains[tmp[1]] & ~(1 << (tmp[2]-1)))
    elif tmp[0] == 3:
        trains[tmp[1]] = (trains[tmp[1]] << 1) & ~(1 << 20)
    elif tmp[0] == 4:
        trains[tmp[1]] = trains[tmp[1]] >> 1

print(len(set(trains[1:])))
