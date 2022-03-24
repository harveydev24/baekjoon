N = int(input())

lst = []

for _ in range(N):
    lst.append(input())

tmp = ''
for i in range(len(lst[0])):
    check = False
    for j in range(N-1):
        if lst[j][i] != lst[j+1][i]:
            tmp += '?'
            check = True
            break

    if not check:
        tmp += lst[0][i]

print(tmp)
