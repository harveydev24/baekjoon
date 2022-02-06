from itertools import permutations
lst = permutations([2,3,4,5,6,7,8,9], 8)
ans = 0
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

for order in lst:
    def rotate(num):
        global first, second, third
        score = 0
        if num == 1:
            score += third
            third = second
            second = first
            first = 1
            return score
        elif num == 2:
            score += third
            score += second
            third = first
            second = 1
            first = 0
            return score
        elif num == 3:
            score += third
            score += second
            score += first
            third = 1
            second = 0
            first = 0
            return score
        else:
            score += third
            score += second
            score += first
            score += 1
            third = 0
            second = 0
            first = 0
            return score

    total_score = 0
    idx = 0
    for ining in array:
        out_cnt = 0
        first = 0
        second = 0
        third = 0
        cnt = 0
        while True:
            if idx < 3:
                real_idx = order[idx]
            elif idx == 3:
                real_idx = 1
            else:
                real_idx = order[idx-1]
            result = ining[real_idx-1]
            if result == 0:
                out_cnt += 1
                idx = (idx+1)%9
                if out_cnt == 3: break
                continue
            total_score += rotate(result)
            idx = (idx+1)%9
            cnt += 1
    ans = max(ans, total_score)

print(ans)
