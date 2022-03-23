A, B, C = map(int, input().split())

def squre(a, b):
    if b == 1:
        return a%C
    
    if b%2 == 0:
        return (squre(a, b//2) ** 2)%C
    else:
        return (squre(a, b//2) * squre(a, b//2+1))%C

print(squre(A,B))