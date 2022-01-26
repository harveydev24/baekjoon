N = int(input())
lst = []

for i in range(N):
    A, B, C, D, E, F = map(int, input().split())
    lst.append([A, B, C, D, E, F])

'''
A,F = 0, 5
B,D = 1, 3
C,E = 2, 4
'''

def findNextNum(lst, curr):
    for idx, item in enumerate(lst):
        if item == curr:
            if idx == 0:
                return lst[5]
            elif idx == 1:
                return lst[3]
            elif idx == 2:
                return lst[4]
            elif idx == 3:
                return lst[1]
            elif idx == 4:
                return lst[2]
            else:
                return lst[0]

ans = 0
for i in range(6):
    tmpMax = 0
    curr = lst[0][i]
    for item in lst:
        next = findNextNum(item, curr)
        tmp = 0
        for num in item:
            if num != curr and num != next:
                tmp = max(num, tmp)
        tmpMax += tmp
        curr = next
    ans = max(tmpMax, ans)
print(ans)