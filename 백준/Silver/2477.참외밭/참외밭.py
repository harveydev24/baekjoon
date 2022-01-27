K = int(input())
lst = []
for i in range(6):
    direction, l = map(int, input().split())
    lst.append([direction, l])

def rotate(lst):
    return lst[1:] + [lst[0]]

while True:
    lst = rotate(lst)
    if lst[0][0] == lst[2][0] and lst[1][0] == lst[3][0]: 
        break

print((lst[4][1]*lst[5][1]-lst[1][1]*lst[2][1])*K)