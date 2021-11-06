def PatternUnlock(N, hits):
    if N < 2:
        return ""
    else:
        xy = {}
        xy[1] = [1.0, 0.0]
        xy[2] = [1.0, 1.0]
        xy[3] = [1.0, 2.0]
        xy[4] = [0.0, 2.0]
        xy[5] = [0.0, 1.0]
        xy[6] = [0.0, 0.0]
        xy[7] = [2.0, 2.0]
        xy[8] = [2.0, 1.0]
        xy[9] = [2.0, 0.0]

        sum_hits = 0.0
        cnt = 0
        while cnt < N - 1:
            dot_c = hits[cnt]
            dot_n = hits[cnt + 1]
            dx = abs(xy[dot_n][0] - xy[dot_c][0])
            dy = abs(xy[dot_n][1] - xy[dot_c][1])
            sum_hits += (dx + dy) ** (1 / 2)
            cnt += 1

        sum_rnd = str(round(sum_hits, 5))
        ans = ""
        for s in sum_rnd:
            if s == "0" or s == ".":
                continue
            else:
                ans += s
        return ans
