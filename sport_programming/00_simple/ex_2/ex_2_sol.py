def odometer(oksana):

    pairs = 0
    vc = 0
    tc = 0
    tp = 0
    S = 0
    
    if len(oksana) % 2 == 0:
        pairs = len(oksana)
    else:
        pairs = len(oksana) - 1
    
    for p in range(pairs):
        if p % 2 == 0:
            vc = oksana[p]
        else:
            tc = oksana[p]
            S += (vc * (tc - tp))
            tp = tc

    return S
