N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
state = [['S']*M for _ in range(N)]
score = 0


def attack(r, c, d):
    global score
    if state[r][c] == 'S':
        if d == 'E':
            c_last_idx = min(M, c+(lst[r][c]))
            while c < c_last_idx:
                if state[r][c] == 'S':
                    score += 1
                    state[r][c] = 'F'
                    c_last_idx = min(M, max(c_last_idx, c+(lst[r][c])))
                c += 1

        elif d == 'W':
            c_last_idx = max(-1, c-(lst[r][c]))
            while c > c_last_idx:
                if state[r][c] == 'S':
                    score += 1
                    state[r][c] = 'F'
                    c_last_idx = max(-1, min(c_last_idx, c-(lst[r][c])))
                c -= 1

        elif d == 'S':
            r_last_idx = min(N, r+(lst[r][c]))
            while r < r_last_idx:
                if state[r][c] == 'S':
                    score += 1
                    state[r][c] = 'F'
                    r_last_idx = min(N, max(r_last_idx, r+(lst[r][c])))
                r += 1
        elif d == 'N':
            r_last_idx = max(-1, r-(lst[r][c]))
            while r > r_last_idx:
                if state[r][c] == 'S':
                    score += 1
                    state[r][c] = 'F'
                    r_last_idx = max(-1, min(r_last_idx, r-(lst[r][c])))
                r -= 1


def defense(r, c):
    state[r][c] = 'S'


for i in range(2*R):
    if i % 2 == 0:
        X, Y, D = input().split()
        attack(int(X)-1, int(Y)-1, D)
    else:
        X, Y = input().split()
        defense(int(X)-1, int(Y)-1)

print(score)
for item in state:
    print(' '.join(item))
