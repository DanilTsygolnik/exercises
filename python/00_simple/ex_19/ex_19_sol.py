def chains(L):
    coord = []
    chain_head = None
    chain_tail = None
    cnt = 0
    while cnt < len(L)-1: # от 0 до предпоследнего включительно
        if L[cnt] == L[cnt+1]:
            if chain_head == None: # если цепь только началась, то chain_head=None --> chain_head=cnt
                chain_head = cnt
            elif cnt == len(L)-2: # текущий эл-т последний эл-т
                chain_tail=cnt+1
                coord.append([chain_head, chain_tail])
            # иначе двигаемся дальше по цепи
        else: 
            if chain_head != None: # последний элемент цепи
                chain_tail = cnt
                coord.append([chain_head, chain_tail])
                chain_head=None
            # если chain_head==None, т.е. не в цепи, то ничего
        cnt += 1
    return coord

def get_data_templ(data_mess):
    # создать пустой словарь
    items = {}
    for i in data_mess: # идем по списку строк data_mess, и далее для каждой
        curr_val = i.split() # curr_val=[item, amount]
        if curr_val[0] not in items:
            items[curr_val[0]] = int(curr_val[1]) # если item попалось первый раз, добавляем в словарь
        else:
            items[curr_val[0]] += int(curr_val[1]) # прибавляем текущее amount к общему кол-во

    # заготовку под сортировку
    data_templ = []
    for i in items.keys():
        data_templ.append([i, items[i]])
    return data_templ

def ShopOLAP(N, data_mess): # получаем список строк, выводим список строк

    sorted_by_amount = sorted(get_data_templ(data_mess), reverse=True, key=lambda x:x[1])
    data_organized = sorted(sorted_by_amount, key=lambda x:x[0])
    return data_organized
