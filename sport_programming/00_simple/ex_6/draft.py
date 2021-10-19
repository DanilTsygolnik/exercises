import random

def rand():
    N = random.randint(0, 6)

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

    hits = []
    output = {}
    if N == 0:
        output['N'] = N
        output['hits'] = hits
    else:
        dot_c = random.randint(1, 9)
        dot_n = None
        cnt = 0
        while cnt < N - 1:
            if hits == []:
                hits += [dot_c]
            else:
                while True:
                    dot_n = random.randint(1, 9)
                    dx = abs(xy[dot_n][0] - xy[dot_c][0])
                    dy = abs(xy[dot_n][1] - xy[dot_c][1])
                    if dx > 1 or dy > 1 or dot_n == dot_c:
                        continue
                    else:
                        hits += [dot_n]
                        dot_c = dot_n
                        break
                cnt += 1
        output['N'] = N
        output['hits'] = hits
    return output

values = rand()
print(values['N'], values['hits'])
