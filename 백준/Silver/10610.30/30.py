n_lst = list(map(int, input()))
n_lst.sort(reverse=True)

if n_lst[-1] != 0 or sum(n_lst[:-1])%3 != 0:
    print(-1)
else:
    print(''.join([str(x) for x in n_lst]))
