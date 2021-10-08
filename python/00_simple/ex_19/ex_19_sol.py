def chains(L):
    coord = []
    chain_head = None
    chain_tail = None
    cnt = 0
    while cnt < len(L)-1:
        if L[cnt] == L[cnt+1]:
            if chain_head == None:
                chain_head = cnt
            if cnt == len(L)-2:
                chain_tail=cnt+1
                coord.append([chain_head, chain_tail])
        else: 
            if chain_head != None:
                chain_tail = cnt
                coord.append([chain_head, chain_tail])
                chain_head=None
        cnt += 1
    return coord

def get_data_templ(data_mess):
    items = {}
    for i in data_mess:
        curr_val = i.split()
        if curr_val[0] not in items:
            items[curr_val[0]] = int(curr_val[1])
        else:
            items[curr_val[0]] += int(curr_val[1])

    data_templ = []
    for i in items.keys():
        data_templ.append([i, items[i]])
    return data_templ

def ShopOLAP(N, data_mess):

    amount_sorted = sorted(get_data_templ(data_mess), reverse=True, key=lambda x: x[1])
    
    amount_list = []
    for i in amount_sorted:
        amount_list.append(i[1])

    coord = chains(amount_list)

    for i in coord:
        curr_sort = sorted(amount_sorted[i[0]:i[1]+1], key=lambda x: x[0])
        amount_sorted = amount_sorted[:i[0]] + curr_sort + amount_sorted[i[1]+1:]

    data_organized = []
    for i in amount_sorted:
        curr_str = i[0] + ' ' + str(i[1])
        data_organized.append(curr_str) 
    return data_organized
