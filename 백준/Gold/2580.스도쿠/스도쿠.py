sdoku = []
for _ in range(9):
    sdoku.append(list(map(int, input().split())))

def possibleNumber(i, j):
    global sdoku
    tmp = []
    res = []
    tmp += sdoku[i]
    tmp += [sdoku[x][j] for x in range(9)]
    ii, jj = (i//3)*3, (j//3)*3
    for x in range(ii, ii+3):
        for y in range(jj, jj+3):
            tmp.append(sdoku[x][y])
    for n in range(1,10):
        if n not in tmp:
            res.append(n)
    return res

zeroPosition = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zeroPosition.append((i,j))

def solve(i, j, idx):
    global sdoku
    pn = possibleNumber(i,j)
    if not pn:
        return
    if idx == len(zeroPosition)-1:
        sdoku[i][j] = pn[0]
        for item in sdoku:
            print(' '.join([str(x) for x in item]))
        exit(0)
    for item in pn:
        sdoku[i][j] = item
        solve(zeroPosition[idx+1][0], zeroPosition[idx+1][1], idx+1)
        sdoku[zeroPosition[idx+1][0]][zeroPosition[idx+1][1]] = 0

solve(zeroPosition[0][0], zeroPosition[0][1], 0)