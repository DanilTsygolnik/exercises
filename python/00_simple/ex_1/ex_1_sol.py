def squirrel(N):

    def fact(n):
    
        def iter(prod, cnt, val):
            if val == 0 or val == 1:
                return 1
            elif cnt > val:
                return prod
            else:
                return iter ((prod * cnt), (cnt + 1), val)
        
        return iter(1, 1, n)
    
    def emeralds(k):
        if k == 0:
            return 0
        elif k < 10:
            return k
        else:
            return emeralds(k // 10)

    if N < 0:
        raise ValueError("N must be equal to or bigger than 0")
    elif type(N) != type(1):
        raise ValueError("N must be integer")
    else:
        return emeralds(fact(N))
