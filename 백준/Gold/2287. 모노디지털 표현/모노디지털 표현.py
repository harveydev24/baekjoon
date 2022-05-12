K = int(input())
n = int(input())

sets = []

for i in range(8):
    if i == 0:
        sets.append(set([K]))
    else:
        tmp = K
        for j in range(i):
            tmp *= 10
            tmp += K

        tmp_set = set([tmp])
        for k in range(i):
            for num1 in sets[k]:
                for num2 in sets[i-k-1]:
                    tmp_set.add(num1+num2)
                    tmp_set.add(num1-num2)
                    tmp_set.add(num1*num2)
                    if num2:
                        tmp_set.add(num1//num2)
        sets.append(tmp_set)
for _ in range(n):
    item = int(input())
    for idx, value in enumerate(sets):
        if item in value:
            print(idx+1)
            break
    else:
        print("NO")
