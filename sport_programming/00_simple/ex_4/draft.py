import random

def MadMax(N, Tele):
    def list_sort(source):
        if len(source) < 2:
            s_list = source
        else:
            m = source[0]
            less = []
            greater = []
            for i in source[1:]:
                if i >= m:
                    greater.append(i)
                else:
                    less.append(i)
            s_list = list_sort(less) + [m] + list_sort(greater)
        
        return s_list

    if N == 1:
        return Tele
    else:
        Tele_sort = list_sort(Tele)
        max_n = Tele_sort[N - 1]
        Tele_output = []
        cnt = 0
        while cnt <= ((N - 2) // 2):
            Tele_output.append(Tele_sort[cnt])
            cnt += 1
        Tele_output.append(max_n)
        cnt = N - 2
        while cnt > ((N - 2) // 2):
            Tele_output.append(Tele_sort[cnt])
            cnt -= 1
    return Tele_output


#for N in range(1, 13, 2):
#    Tele = []
#    cnt = 0
#    while cnt < N:
#        Tele.append(random.randint(0,255))
#        cnt += 1
#    print("MadMax(" + str(N) + "," + str(Tele) + ")")
#    print(MadMax(N, Tele))

# -- output examples --
#MadMax(1,[49])
#[49]
#MadMax(3,[3, 209, 81])
#[3, 209, 81]
#MadMax(5,[78, 90, 95, 204, 19])
#[19, 78, 204, 95, 90]
#MadMax(7,[98, 132, 56, 21, 16, 171, 122])
#[16, 21, 56, 171, 132, 122, 98]
#MadMax(9,[35, 172, 61, 179, 108, 144, 212, 114, 105])
#[35, 61, 105, 108, 212, 179, 172, 144, 114]
#MadMax(11,[27, 173, 184, 18, 194, 57, 72, 124, 69, 135, 208])
#[18, 27, 57, 69, 72, 208, 194, 184, 173, 135, 124]
