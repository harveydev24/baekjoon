N, B = map(int, input().split())
A = [[] for _ in range(N)]
for i in range(N):
    A[i].extend(list(map(int, input().split())))

def mul(lst, lst2):
    res = 0
    for i in range(N):
        res += lst[i] * lst2[i]
        res %= 1000
    return res

def transpose(A):
    return list(zip(*A))

def matmul(A, B):
    res = [[] for _ in range(N)]
    i = 0
    for item in A:
        for item2 in B:
            res[i].append(mul(item, item2))
        i += 1
    return res

def solve(B):
    pass

def seperate(B):
    if B == 1: return '1'
    if B % 2 == 1: return seperate(B//2) + '1' 
    else: return seperate(B//2) + '0'

resMul = [A]
a = seperate(B)

while len(resMul) != len(a):
    resMul.append(matmul(resMul[-1], transpose(resMul[-1])))
a = a[::-1]
res = []
for idx, item in enumerate(a):
    if item == '1':
        if not res:
            res = resMul[idx]
        else:
            res = matmul(res, transpose(resMul[idx]))

for item in res:
    print(' '.join([str(x%1000) for x in item]))

