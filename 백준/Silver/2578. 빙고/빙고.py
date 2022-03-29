arr = [list(map(int, input().split())) for _ in range(5)]


def check():
    cnt = 0
    for r in range(5):
        tmp = 0
        for c in range(5):
            if arr[r][c] in check_st:
                tmp += 1
        if tmp == 5:
            cnt += 1

    for c in range(5):
        tmp = 0
        for r in range(5):
            if arr[r][c] in check_st:
                tmp += 1
        if tmp == 5:
            cnt += 1

    tmp = 0
    for i in range(5):
        if arr[i][i] in check_st:
            tmp += 1
    if tmp == 5:
        cnt += 1

    tmp = 0
    for i in range(5):
        if arr[i][4-i] in check_st:
            tmp += 1
    if tmp == 5:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


sequence = []

for _ in range(5):
    sequence.extend(list(map(int, input().split())))

check_st = set()

for i in range(25):
    check_st.add(sequence[i])

    if check():
        print(i+1)
        break
