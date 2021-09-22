def ConquestCampaign(N, M, L, battalion):

    def add_pair(n, m, targetDict):
        targetDict[str(n) + ", " + str(m)] = [n, m]
    
    def uniqueList(valuesList, targetDict):
        ind = 0
        for i in valuesList:
            if ind % 2 == 0:
                nc = i
            else:
                mc = i
                if targetDict.get(str(nc) + ", " + str(mc)) == None:
                    add_pair(nc, mc, targetDict)
            ind += 1

    ind = 0
    day = 0
    A = N*M

    Lc = {}
    S = {}
    Ln = {}

    uniqueList(battalion, Lc)

    while A > 0:
        for l in Lc:
            ind = 0
            while ind < 2:
                coord = Lc[l][ind]
                if coord == 1:
                    if ind == 0:
                        moves_n = coord + 1
                    else:
                        moves_m = coord + 1
                else:
                    if ind == 0:
                        if coord == N:
                            moves_n = coord - 1
                        else:
                            moves_n = [coord + 1, coord - 1]
                    else:
                        if coord == M:
                            moves_m = coord - 1
                        else:
                            moves_m = [coord + 1, coord - 1]
                ind += 1

            if type(moves_n) == type(1):
                add_pair(moves_n, Lc[l][1], Ln)
            else:
                for n in moves_n:
                    add_pair(n, Lc[l][1], Ln)

            if type(moves_m) == type(1):
                add_pair(Lc[l][0], moves_m, Ln)
            else:
                for m in moves_m:
                    add_pair(Lc[l][0], m, Ln)

        d_list = []
        for k in Ln.keys():
            if (k in S) or (k in Lc):
                d_list.append(k)

        for d in d_list:
            del Ln[d]

        A -= len(Lc.keys())

        for k in Lc.keys():
            S[k] = Lc[k]

        Lc.clear()

        for k in Ln.keys():
            Lc[k] = Ln[k]

        Ln.clear()

        day += 1

    return day
