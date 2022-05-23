N, M = map(int, input().split())
dct = dict()
dct2 = dict()
for i in range(1, N+1):
    pokemon = input()
    dct[pokemon] = i
    dct2[i] = pokemon


for _ in range(M):
    tmp = input()
    if tmp.isalpha():
        print(dct.get(tmp))
    else:
        print(dct2.get(int(tmp)))
