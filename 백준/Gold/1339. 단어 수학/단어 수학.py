N = int(input())

cnt_dict = {}
for i in range(65, 91):
    cnt_dict[chr(i)] = 0

for _ in range(N):
    characters = list(input())
    tmp = 1

    for i in range(len(characters)-1 ,-1, -1):
        cnt_dict[characters[i]] += tmp
        tmp *= 10

lst = list(cnt_dict.items())
lst.sort(key=lambda x: x[1], reverse=True)

tmp = 9
ans = 0

for item in lst:
    ans += cnt_dict[item[0]]*tmp
    tmp -= 1

print(ans)