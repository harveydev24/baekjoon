N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

def check(paper):
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] != paper[0][0]: return False
    return True


w = 0
b = 0

def solve(paper):
    global w
    global b
    if len(paper) == 1 or check(paper): 
        if paper[0][0] == 1: b += 1
        else: w += 1
    else:
        lu = []
        ru = []
        ld = []
        rd = []
        for i in range(int(len(paper)/2)):
            lu.append(paper[i][:int(len(paper)/2)])
            ru.append(paper[i][int(len(paper)/2):])
        for i in range(int(len(paper)/2), len(paper)):
            ld.append(paper[i][:int(len(paper)/2)])
            rd.append(paper[i][int(len(paper)/2):])
        solve(lu)
        solve(ru)
        solve(ld)
        solve(rd)
        
solve(paper)
print(w)
print(b)
        
