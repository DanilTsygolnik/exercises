def get_strings(string):
    curr_str = string
    strings = []
    while curr_str != '':
        index_cnt = 0
        curr_word = ''
        while index_cnt < len(curr_str):
            if curr_str[index_cnt] == ' ':
                break
            else:
                curr_word += curr_str[index_cnt]
                index_cnt += 1
        if curr_word != '':
            strings.append(curr_word)
        if (index_cnt + 1) > len(curr_str):
            break
        else:
            curr_str = curr_str[index_cnt+1:]
    return strings

# индексы начала i-й строки из tanks_coord в j-й строке map_coord
def find_all(string, word):
    curr_index = 0
    indexes = []
    while curr_index >= 0:
        search_result = string[curr_index:].find(word)
        if search_result >= 0:
            indexes.append(curr_index + search_result)
            curr_index += search_result + len(word)
        else:
            curr_index = search_result
    return indexes

# ищем слова из words в строках strings
def get_search_res(strings, words):
    H1 = len(strings)
    H2 = len(words)
    search_res = []
    # для текущего слова
    i = 0
    while i < H2:
        j = i  # не каждое слово из массива words имеет смысл искать с самой первой строки в strings 
        search_res_line = []
        while j <= H1 - H2 + i: # не каждое слово из массива words имеет смысл искать ниже определенной строки в strings
            k_indexes = find_all(strings[j], words[i])
            for k in k_indexes:
                search_res_line.append([i, j, k])
            j += 1
        search_res.append(search_res_line)
        i += 1
    return search_res

def TankRush(H1, W1, Map, H2, W2, tanks):
    Map_strings = get_strings(Map)
    tanks_strings = get_strings(tanks)
    s_res = get_search_res(Map_strings, tanks_strings)
    
    is_in = False
    if H1*W1 == 0 or H2*W2 == 0:
        if Map == tanks:
            is_in = True
        else:
            is_in = False
    if Map_strings == tanks_strings:
        is_in = True
    else:
        if Map_strings == [] or tanks_strings == []:
            is_in = False
        else:
            # по данным из s_res определяем значение is_in
            # s_res -- i0 i1 i2 ... у каждого есть набор k, причем каждого k строго по одному --> и j по одному
            col_indexes = []
            j_ref = []
            for i in s_res[0]:
                j_ref.append(i[1])
                col_indexes.append(i[2])
            ref_index = 0
            for k in col_indexes:
                j_list = [j_ref[ref_index]]
                for i in s_res: # для каждой i-й строки из tanks...
                    for j in i: # ...среди всех найденных позиций i-й строки в map...
                        if j[2] == k: # ...ищем совпадение по текущему k
                            if j[1] == j_list[len(j_list)-1] + 1:
                                j_list.append(j[1])
                                break # перебирать далее смысла нет, т.к. для данных i-й строки и столбца k единств. верное j найдено 
                ref_index +=1 # на случай перехода к сл. k

                # здесь должен получиться j_list j из каждого i для данного k
                if len(j_list) == H2:
                    is_in = True
                    break
    return is_in
