import sys
sys.setrecursionlimit(10**5)

pre_order = []
tree = {}

while True:
    try:
        tmp = int(input())
        pre_order.append(tmp)
        tree[tmp] = [-1, -1]
    except:
        break


def findParent(start, end):
    left_start, left_end, right_start, right_end = -1, end, -1, end
    for i in range(start+1, end):
        if tree[pre_order[start]][0] == -1 and pre_order[i] < pre_order[start]:
            tree[pre_order[start]][0] = pre_order[i]
            left_start = i
        if tree[pre_order[start]][1] == -1 and pre_order[i] > pre_order[start]:
            tree[pre_order[start]][1] = pre_order[i]
            right_start = i
            left_end = i

    if left_start != -1:
        findParent(left_start, left_end)
    if right_start != -1:
        findParent(right_start, right_end)


findParent(0, len(pre_order))


def post_order(x):
    if x != -1:
        post_order(tree[x][0])
        post_order(tree[x][1])
        print(x)


if pre_order:
    post_order(pre_order[0])
