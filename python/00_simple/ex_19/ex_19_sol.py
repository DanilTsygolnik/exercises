def get_item_name_and_num(orig_name):
    index = 0
    numbers = []
    item_data = []
    for i in range(10):
        numbers += [str(i)]
    for i in orig_name:
        if i in numbers: # если в строке есть цифры, записываем item_data=[name, num] по текущему index'у
            item_data.append(orig_name[0:index])
            item_data.append(int(orig_name[index:]))
            break
        index += 1
    if item_data == []: # если в строке нет цифр, считываем строку, вместо цифры добавляем пустую строку
        item_data.append(orig_name)
        item_data.append(-1)
    return item_data
     

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
        name_num = get_item_name_and_num(i)
        data_templ.append([name_num[0], name_num[1], items[i]])
    return data_templ

def ShopOLAP(N, data_mess): # получаем список строк, выводим список строк

    #sorted_by_amount = sorted(get_data_templ(data_mess), reverse=True, key=lambda x:x[1])
    #data_organized = sorted(sorted_by_amount, key=lambda x:x[0])
    data_organized = sorted(sorted(get_data_templ(data_mess)), key=lambda x: ((x[2], reverse=True),x[0],x[1]))
    return data_organized

# дописать блок преобразования data_org=[[], [], ... []] в data_org=[str1, str2, ...] 
#def get_output(data_org)
#    output = []
#    for i in data_org:
#        output.append(i[0]+i[1])
#    return output
