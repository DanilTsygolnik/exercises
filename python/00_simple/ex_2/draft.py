def odometer(oksana):

    errors = 0

    if type(oksana) != type([]):
        return ValueError("Argument must be <class 'list'>")

    # 1) len(oksana) < 2; example: [65]
    if len(oksana) < 2:
        return ValueError("List must contain at least 2 elements")

    for i in oksana:
        # 2) negative numbers in list; example [40 -1] or [-24 6]
        if i < 0:
            break
            return ValueError("List must contain only positive integers")
        # 3) wrong types in list; example [35.6 5] etc.
        elif type(i) != type(1):
            break
            return ValueError("List must contain only integers")
        else:
            continue

    # oksana type/value ok
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
