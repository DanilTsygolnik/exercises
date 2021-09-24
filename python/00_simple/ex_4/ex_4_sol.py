def MadMax(N, Tele):
    if N == 1:
        return Tele
    else:
        Tele.sort()
        output = Tele[:((N - 2) // 2 + 1)]
        right = Tele[((N - 2) // 2 + 1):(N - 1)]
        right.reverse()
        output += [Tele[N - 1]] + right
    return output
