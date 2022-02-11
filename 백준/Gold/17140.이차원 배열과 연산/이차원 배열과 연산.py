import copy
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def mySort(lst):
    sorted_lst = []
    cnt_dct = {}
    tmp_lst = []
    for n in lst:
        if n == 0: continue
        if cnt_dct.get(n) == None:
            cnt_dct[n] = 1
        else:
            cnt_dct[n] += 1

    for n, cnt in cnt_dct.items():
        tmp_lst.append((cnt,n))

    tmp_lst.sort()

    if len(tmp_lst)>50:
        for cnt, n in tmp_lst[50:]:
            sorted_lst.extend([n, cnt])
    else:
        for cnt, n in tmp_lst:
            sorted_lst.extend([n, cnt])
    
    return sorted_lst

def R():
    max_len = 0
    for i in range(len(A)):
        A[i] = mySort(A[i])
        max_len = max(max_len, len(A[i]))

    for i in range(len(A)):
        while len(A[i])<max_len:
            A[i].append(0)

def C():
    global A
    max_len = 0
    A_t =list(zip(*A))
    for i in range(len(A_t)):
        A_t[i] = mySort(A_t[i])
        max_len = max(max_len, len(A_t[i]))

    for i in range(len(A_t)):
        while len(A_t[i])<max_len:
            A_t[i].append(0)
    
    A = list(zip(*A_t))

t = 0

while True:
    if 0<=r-1<len(A) and 0<=c-1<len(A[0]):
        if A[r-1][c-1] == k:
            break
    if t>=100:
        print(-1)
        exit(0)
    if len(A) >= len(A[0]):
        R()
    else:
        C()
    t += 1
   

print(t)
