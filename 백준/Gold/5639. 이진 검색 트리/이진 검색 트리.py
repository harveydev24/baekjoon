import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**9))
tree = []
res = []
def solve(tree, left, right):
    if left > right:
        return
    root = tree[left]
    leftStart = left + 1
    rightEnd = right
    rightStart = right + 1
    for i in range(right - left + 1):
        if i == 0: continue
        if tree[left+i] > root:
            rightStart = i + left
            break
    leftEnd = rightStart-1
    solve(tree, leftStart, leftEnd)
    solve(tree, rightStart, rightEnd)
    res.append(root)

while True:
    try:
        a = int(input())
        tree.append(a)
    except:
        break
solve(tree, 0, len(tree)-1)
for item in res:
    print(item)