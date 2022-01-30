w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dx = t%(2*w)
dy = t%(2*h)

if dx <= w-p:
    p += dx
elif w-p < dx <= 2*w-p:
    p = w - (dx - (w - p))
else:
    p = 0 + (dx - 2 * (w - p) - p)

if dy <= h-q:
    q += dy
elif h-q < dy <= 2*h-q:
    q = h - (dy - (h - q))
else:
    q = 0 + (dy - 2 * (h - q) - q)

print(p, q)