def makePi(pattern):
    pi = [0]*len(pattern)
    j, i = 0, 1

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                pi[i] = 0
                i += 1
    return pi

def KMP(pattern, string):
    pi = makePi(pattern)
    i, j = 0, 0
    cnt = 0
    idx = []
    while i < len(string):
        if pattern[j] == string[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                i += 1
        if j == len(pattern):
            cnt += 1
            idx.append(i-j+1)
            j = pi[j-1]
            
    return cnt, idx

T = input()
P = input()

cnt, idx = KMP(P, T)
print(cnt)
print(' '.join([str(x) for x in idx]))