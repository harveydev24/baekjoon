# 7
# WINNT\SYSTEM32\CONFIG
# GAMES
# WINNT\DRIVERS
# HOME
# WIN\SOFT
# GAMES\DRIVERS
# WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86


N = int(input())
directories = [input().split("\\") for _ in range(N)]
directories.sort()


dct = {}
for directory in directories:
    curr = dct
    for item in directory:
        if curr.get(item) == None:
            curr[item] = {}
        curr = curr[item]
        curr['printed'] = False
    curr['printed'] = False


for directory in directories:
    curr = dct
    for idx, item in enumerate(directory):
        if curr[item].get('printed') == False:
            curr[item]['printed'] = True
            print(' '*idx + item)
        curr = curr[item]
