N = int(input())

positive = []
negative = []
zero = []

for _ in range(N):
    n = int(input())
    if n > 0:
        positive.append(n)
    elif n == 0:
        zero.append(n)
    else:
        negative.append(n)

positive.sort()
negative.sort(reverse=True)

ans = 0

while True:
    if len(positive) >= 2:
        if positive[-2] >= 2:
            ans += positive[-1]*positive[-2]
            positive.pop()
            positive.pop()
        else:
            ans += sum(positive)
            break
    else:
        ans += sum(positive)
        break


while True:
    if len(negative) >= 2:
        ans += negative[-2]*negative[-1]
        negative.pop()
        negative.pop()
    else:
        if not zero:
            ans += sum(negative)
        break

print(ans)
