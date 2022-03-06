from cgi import test


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    visited = [False]*(2*N)
    ans = []
    for i in range(2*N):
        if not visited[i]:
            visited[i] = True

            for j in range(i+1,2*N):
                if not visited[j] and lst[j]//4*3 == lst[i]:
                    visited[j] = True
                    ans.append(lst[i])
                    break

    print(f'Case #{test_case}:', end=' ')
    print(*ans)   
