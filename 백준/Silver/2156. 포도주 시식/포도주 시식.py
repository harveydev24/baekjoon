n = int(input())

wine = [0]*n

for i in range(n):
    wine[i] = int(input())

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp = [[0, 0, 0, 0, 0] for _ in range(n)]
    dp[0][0] = wine[0]
    dp[0][3] = wine[0]
    dp[1][0] = dp[0][0]
    dp[1][1] = wine[1]
    dp[1][2] = dp[0][2]
    dp[1][3] = wine[0]+wine[1]
    dp[1][4] = wine[1]
    dp[2][0] = wine[0] + wine[2]
    dp[2][1] = wine[1] + wine[2]
    dp[2][2] = wine[2]
    dp[2][3] = dp[1][3]
    dp[2][4] = dp[1][4]

    for i in range(3, n):
        dp[i][0] = max([dp[i-1][3]+wine[i], dp[i-1][4]+wine[i]])
        dp[i][1] = max([dp[i-1][0]+wine[i], dp[i-1][2]+wine[i]])
        dp[i][2] = max([dp[i-2][3]+wine[i], dp[i-2][4] + wine[i]])
        dp[i][3] = dp[i-1][1]
        dp[i][4] = max([dp[i-1][0], dp[i-1][2]])

    print(max([max(x) for x in dp]))
