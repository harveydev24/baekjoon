N = int(input())

for _ in range(N):
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A_ = sorted(A[1:], reverse=True)
    B_ = sorted(B[1:], reverse=True)
    
    length = min(len(A_), len(B_))

    for i in range(length):
        if A_[i] > B_[i]:
            print('A')
            break
        elif A_[i] < B_[i]:
            print('B')
            break
        else:
            if i == length-1:
                if len(A_) > len(B_):
                    print('A')
                    break
                elif len(A_) < len(B_):
                    print('B')
                    break
                else:
                    print('D')
                    break