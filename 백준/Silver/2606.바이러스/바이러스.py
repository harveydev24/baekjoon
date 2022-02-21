N = int(input())
M = int(input())

network = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

virus = [False for _ in range(N+1)]

def DFS(n):
    if not virus[n]: 
        virus[n] = True
    else: return
    for i in network[n]:
        DFS(i)
    
        
DFS(1)
sum = 0
for i in range(1,N+1):
    if virus[i] == True: sum += 1

print(sum-1)