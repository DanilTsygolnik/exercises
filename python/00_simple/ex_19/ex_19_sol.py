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

# дописать блок преобразования data_org=[[], [], ... []] в data_org=[str1, str2, ...] 
#def get_output(data_org)
#    output = []
#    for i in data_org:
#        output.append(i[0]+i[1])
#    return output
