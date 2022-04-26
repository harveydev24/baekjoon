import sys
input = sys.stdin.readline
R, S = map(int, input().split())
lst = []
m_lst = []
g_lst = []
for r in range(R):
    tmp = input().rstrip()
    for c in range(S):
        if tmp[c] == '#':
            g_lst.append((r, c))
        if tmp[c] == 'X':
            m_lst.append((r, c))
    lst.append(tmp)
dist = 10**5
for c in range(S):
    tmp_dist = 10**5
    m_pos = -1
    for r in range(R):
        if lst[r][c] == 'X':
            m_pos = r

        if lst[r][c] == '#':
            if m_pos != -1:
                tmp_dist = min(tmp_dist, r-m_pos-1)
    dist = min(dist, tmp_dist)


ans = [['.']*S for _ in range(R)]
for r, c in g_lst:
    ans[r][c] = '#'

for r, c in m_lst:
    ans[r+dist][c] = 'X'


for row in ans:
    print(''.join(row))