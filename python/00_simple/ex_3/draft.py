
def add_pair(n, m, targetDict):
    targetDict[str(n) + ", " + str(m)] = [n, m]

def uniqueList(valuesList, targetDict): # <class 'list'>, <class 'dict'>

    ind = 0

    for i in valuesList:
        if ind % 2 == 0:
            nc = i
        else:
            mc = i
            # подготовка списка точек высадки
            if targetDict.get(str(nc) + ", " + str(mc)) == None:
                add_pair(nc, mc, targetDict)
        ind += 1

def ConquestCampaign(N, M, L, battalion):

    # variables for further procedures
    ind = 0
    day = 0
    A = N*M

    # current day coordinates
    Lc = {}
    # filled squares
    S = {}
    # next day coordinates
    Ln = {}

    # unique coordinates from initial input (battalion) --> Lc, day 0
    uniqueList(battalion, Lc)

    # conquest cycle
    while A > 0:
        for l in Lc: # считывание под запись в Ln
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
            # запись ходов по n в Ln
            if type(moves_n) == type(1):
                add_pair(moves_n, Lc[l][1], Ln)
            else:
                for n in moves_n:
                    add_pair(n, Lc[l][1], Ln)
            # запись ходов по m в Ln
            if type(moves_m) == type(1):
                add_pair(Lc[l][0], moves_m, Ln)
            else:
                for m in moves_m:
                    add_pair(Lc[l][0], m, Ln)

        # проверка дубликатов в S{}, Lc{}
        d_list = []
        for k in Ln.keys():
            if (k in S) or (k in Lc):
                d_list.append(k)

        # удаление дубликатов из Ln
        for d in d_list:
            del Ln[d]

        # preparations for the next day
        # обновить А - вычесть кол-во квадратов, которые пойдут в S
        A -= len(Lc.keys())

        # перенос ключей из Lc в S (захват областей в текущем дне)
        for k in Lc.keys():
            S[k] = Lc[k]

        # очистка Lc под координаты для следующего дня
        Lc.clear()

        # запись плана захвата следующего дня
        for k in Ln.keys():
            Lc[k] = Ln[k]

        # очистка Ln для следующего дня
        Ln.clear()

        # смена суток, переход к сл дню
        day += 1

    return day

#print(ConquestCampaign(3, 3, 3, [1, 1, 2, 2, 3, 3]))
