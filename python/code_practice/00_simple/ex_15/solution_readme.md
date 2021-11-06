## Задача

В качестве входных данных выступают 2 массива.    
Реализовать функцию, которая возвращает `True`, если второй массив (в двумерном виде) входит в первый, и `False` - в противном случае.

### Ранние рассуждения

```
def TankRush(H1, W1, Map_strings, H2, W2, tanks_strings) -> bool:

     W1
    ____         W2
  | 1234         __
H1| 2345     H2| 34
  | 0987       | 98

Map_strings   tanks_strings

Исходные данные поступают в виде строк вида:
Map_strings = '1234 2345 0987'
tanks_strings = '34 98'

```

Чтобы реализовать функцию, нужно описать и четко различить следующие ситуации в терминах координат (номер строки, номер столбца):
1) `tanks_strings` не входив массив `Map_strings`: хотя бы одна строка из `tanks_strings` не содержится в `Map_strings`.
2) все строки `tanks_strings` содержатся в `Map_strings`, но не представлены двумерным массивом:
    a) расположены в соседних строках, но сдвинуты по горизонтали;
    b) не располагаются в соседних строках либо столбцах;
3) `tanks_strings` входив массив `Map_strings`.

`tanks_strings` входит в `Map_strings` при соблюдении условий:     
1) присутствие всех строк в Map_strings;
2) индекс каждой сл. строки должен быть больше предыдущего на 1;
3) началу каждой строки (нулевому элементу) должен соответствовать один и тот же индекс столбца в `Map_strings`.

**Внимание:** одна строка из `tanks_strings` может быть представлена в строке из `Map_strings` несколько раз.    
Возможные варианты:
1) может присутствовать в нескольких строках;
2) может присутствовать несколько раз в отдельной строке.


### Код решения

```python

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

# индексы начала i-й строки из tanks_strings в j-й строке Map_strings
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

# ищем каждое слова из второго массива (words[i]) в каждой строке (strings[j]) основного
def get_search_res(strings, words):
    H1 = len(strings)
    H2 = len(words)
    search_res = [] # заготовка вывода функции
    i = 0
    # перебор по словам из списка words
    while i < H2: 
        j = i  # не каждое слово имеет смысл искать с самой первой строки из strings
               # например, если words - матрица высотой H2 = 3, то строки из ее 3-й строки можно не искать в 1 и 2 строках strings...
               # ... если массив words содержится в массиве strings 
        search_res_line = []
        while j <= H1 - H2 + i: # не каждое слово из массива words имеет смысл искать ниже определенной строки в strings
               # например, если массив words высотой H2 содержится в массиве strings, то i1 будет располагаться не ниже j=H1-H2+1
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
            # s_res = [ 
            #            [результаты поиска i0]
            #            [результаты поиска i1]
            #            [результаты поиска i2]
            #            ...
            #            [результаты поискаi(H2-1)]  -- всего H2 списков
            #         ]
            # у каждой i-й строки свой набор k, причем у каждого k строго по одному --> и j по одному

            col_indexes = []
            j_ref = []
            for i in s_res[0]:
                j_ref.append(i[1]) # номера j-х строк, в которых найдена 0-я строка из tanks
                col_indexes.append(i[2]) # набор k
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
```
