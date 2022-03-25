from collections import deque

T = int(input())


def solve(data):
    check = deque(['A', 'F', 'C'])
    check_lst = {'A', 'B', 'C', 'D', 'E', 'F'}

    data_modified = ''

    for letter in data:
        if not data_modified:
            data_modified += letter
        else:
            if letter != data_modified[-1]:
                data_modified += letter
    if data_modified[0] in check_lst and ('AFC' == data_modified[:3] or 'AFC' == data_modified[1:4]) and data_modified[-1] in check_lst:
        return 'Infected!'
    else:
        return 'Good'


res = []
for _ in range(T):
    data = input()

    res.append(solve(data))

for item in res:
    print(item)
