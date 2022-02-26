x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def solve(x, y, x3, y3, x4, y4):
    return (y-y3)*(x4-x3) - (y4-y3)*(x-x3)

if solve(x1, y1, x3, y3, x4, y4)*solve(x2, y2, x3, y3, x4, y4) < 0 and solve(x3, y3, x1, y1, x2, y2)*solve(x4, y4, x1, y1, x2, y2) < 0:
    print(1)
else:
    print(0)