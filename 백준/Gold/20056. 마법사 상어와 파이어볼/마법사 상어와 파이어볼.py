N, M, K = map(int, input().split())

fire_balls = {}

dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls[(r, c)] = [(m, s, d)]

for _ in range(K):
    tmp = {}
    next_fire_balls = {}

    for key, value in fire_balls.items():
        r, c = key
        cnt = len(value)

        if cnt >= 2:
            for i in range(cnt):
                m, s, d = value[i]
                rr, cc = (r+dr[d]*s-1) % N+1, (c+dc[d]*s-1) % N+1
                if not tmp.get((rr, cc)):
                    tmp[(rr, cc)] = [(m, s, d)]
                else:
                    tmp[(rr, cc)].append((m, s, d))
        else:
            m, s, d = value[0]
            rr, cc = (r+dr[d]*s-1) % N+1, (c+dc[d]*s-1) % N+1
            if not tmp.get((rr, cc)):
                tmp[(rr, cc)] = [(m, s, d)]
            else:
                tmp[(rr, cc)].append((m, s, d))

    for key, value in tmp.items():
        r, c = key
        cnt = len(value)
        if cnt >= 2:
            diffusion_direction = 0  # 0->상하좌우, 1-> 대각선
            check = value[0][2] % 2
            m_sum, s_sum = 0, 0
            for m, s, d in value:
                m_sum += m
                s_sum += s
                if check != (d % 2):
                    diffusion_direction = 1

            m = m_sum//5
            if m == 0:
                continue
            s = s_sum//cnt

            # 상하좌우
            if diffusion_direction == 0:
                for d in [0, 2, 4, 6]:
                    if not next_fire_balls.get((r, c)):
                        next_fire_balls[(r, c)] = [(m, s, d)]
                    else:
                        next_fire_balls[(r, c)].append((m, s, d))
            # 대각선
            else:
                for d in [1, 3, 5, 7]:
                    if not next_fire_balls.get((r, c)):
                        next_fire_balls[(r, c)] = [(m, s, d)]
                    else:
                        next_fire_balls[(r, c)].append((m, s, d))
        else:
            next_fire_balls[key] = value

    fire_balls = next_fire_balls

ans = 0

for value in fire_balls.values():
    for m, s, d in value:
        ans += m

print(ans)
