A, B = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


z = gcd(A, B)

i = 1
while True:
    if (z*i) % A == 0 and (z*i) % B == 0:
        break
    i += 1

print(z)
print(z*i)