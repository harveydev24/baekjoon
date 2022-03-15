A, B = map(int, input().split())
C = int(input())
a = C//60
b = C % 60

A = (A + a + (B+b)//60) % 24
B = (B+b) % 60

print(A, B)
