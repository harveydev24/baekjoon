import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
arr = [[]]+[(['X']+list(input().rstrip())) for _ in range(M)]

dp = [[{'J': 0, 'O': 0, 'I': 0} for i in range(N+1)] for _ in range(M+1)]

for r in range(1, M+1):
    for c in range(1, N+1):
        dp[r][c]['J'] = dp[r-1][c]['J']
        dp[r][c]['O'] = dp[r-1][c]['O']
        dp[r][c]['I'] = dp[r-1][c]['I']
        dp[r][c]['J'] += dp[r][c-1]['J']
        dp[r][c]['O'] += dp[r][c-1]['O']
        dp[r][c]['I'] += dp[r][c-1]['I']
        dp[r][c]['J'] -= dp[r-1][c-1]['J']
        dp[r][c]['O'] -= dp[r-1][c-1]['O']
        dp[r][c]['I'] -= dp[r-1][c-1]['I']
        dp[r][c][arr[r][c]] += 1

for _ in range(K):
    a, b, c, d = map(int, input().split())

    j = dp[c][d]['J'] + dp[a-1][b-1]['J'] -\
        dp[a-1][d]['J'] - dp[c][b-1]['J']
    o = dp[c][d]['O'] + dp[a-1][b-1]['O'] -\
        dp[a-1][d]['O'] - dp[c][b-1]['O']
    i = dp[c][d]['I'] + dp[a-1][b-1]['I'] -\
        dp[a-1][d]['I'] - dp[c][b-1]['I']

    print(j, o, i)
