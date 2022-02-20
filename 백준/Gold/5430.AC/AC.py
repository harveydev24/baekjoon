T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    lst_raw = input()
    isEmpty = False
    isNext = False
    lst = ['[']
    tmp = ''

    for i in range(len(lst_raw)):
        if i == 0 or i == len(lst_raw)-1: 
            continue
        if lst_raw[i] != ',':
            tmp += lst_raw[i]
        elif lst_raw[i] == ',':
            lst.append(tmp)
            tmp = ''
        
        if i == len(lst_raw)-2 and tmp != '':
            lst.append(tmp)
    lst += [']']
    if len(lst) == 2: isEmpty = True
    start = 1
    end = len(lst)-2
    for order in p:
        if order == 'R':
            start, end = end, start
        else:
            if isEmpty == True:
                print('error')
                isNext = True
                break
            if start == end:
                isEmpty = True
            elif start < end:
                start += 1
            else:
                start -= 1
    
    if not isNext:
        if not isEmpty:
            if start<=end:
                print('[' + ','.join(lst[start:end+1]) + ']')
            else:
                print('[' + ','.join(lst[end:start+1][::-1]) + ']')
        else:
            print('[]')
    
            