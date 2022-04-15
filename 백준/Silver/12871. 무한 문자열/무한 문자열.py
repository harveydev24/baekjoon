s = input()
t = input()

s_len = len(s)
t_len = len(t)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


tmp = s_len*t_len//gcd(s_len, t_len)

s_ = ''
t_ = ''
while len(s_) != tmp:
    s_ += s
while len(t_) != tmp:
    t_ += t

if s_ == t_:
    print(1)
else:
    print(0)
