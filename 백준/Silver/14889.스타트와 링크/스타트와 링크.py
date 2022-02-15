from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

selectedTeam = combinations(range(N), int(N/2))
tmpMin = float('inf')
for team in selectedTeam:
    nonTeam = []
    for i in range(N):
        if i not in team:
            nonTeam.append(i)
    selectedPower = 0
    nonPower = 0
    tmpCombSelected = list(combinations(team, 2))
    tmpCombNon = list(combinations(nonTeam, 2))
    for j in range(len(tmpCombSelected)):
        selectedPower += (S[tmpCombSelected[j][0]][tmpCombSelected[j][1]] + S[tmpCombSelected[j][1]][tmpCombSelected[j][0]])
        nonPower += (S[tmpCombNon[j][0]][tmpCombNon[j][1]] + S[tmpCombNon[j][1]][tmpCombNon[j][0]])
    tmpMin = min(abs(selectedPower-nonPower), tmpMin)

print(tmpMin)