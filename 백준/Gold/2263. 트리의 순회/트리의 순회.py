import sys
sys.setrecursionlimit(10**5)
n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def solve(startIdx, endIdx, postIdx):
    if startIdx > endIdx: return
    print(postorder[postIdx], end=" ")
    if startIdx == endIdx: return

    rootIdx = inorder.index(postorder[postIdx])
    leftRootIdx = postIdx - (endIdx - rootIdx) - 1
    rightRootIdx = postIdx - 1
    
    solve(startIdx, rootIdx-1, leftRootIdx)
    solve(rootIdx+1, endIdx, rightRootIdx)

solve(0, n-1, n-1)