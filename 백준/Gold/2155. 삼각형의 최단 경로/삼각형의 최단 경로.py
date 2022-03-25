A, B = map(int, input().split())

if B <= A:
    A, B = B, A

ar = 1

while ar**2 < A:
    ar += 1

ac = A-(ar-1)**2

br = 1

while br**2 < B:
    br += 1

bc = B-(br-1)**2-(br-ar)

dr = abs(ac-bc)


if ar**2 % 2 == A % 2:
    if br-ar > dr:
        if ar**2 % 2 == br**2 % 2:
            if B % 2 == br**2 % 2:
                ans = 2*(br-ar)
            else:
                ans = 2*(br-ar) - 1
        else:
            if B % 2 == br**2 % 2:
                ans = 2*(br-ar)
            else:
                ans = 2*(br-ar) - 1
    else:
        ans = abs(br-ar) + abs(bc-ac)

else:
    if br-ar > dr:
        if ar**2 % 2 == br**2 % 2:
            if B % 2 == br**2 % 2:
                ans = 2*(br-ar) + 1
            else:
                ans = 2*(br-ar)
        else:
            if B % 2 == br**2 % 2:
                ans = 2*(br-ar) + 1
            else:
                ans = 2*(br-ar)
    else:
        ans = abs(br-ar) + abs(bc-ac)

print(ans)
