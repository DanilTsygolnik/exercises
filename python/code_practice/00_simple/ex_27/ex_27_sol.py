"""
Написать функцию Football(int F[], int N).

На вход функция получает массив F из N (N >= 1) целых неповторяющихся чисел.
Функция возвращает true, если массив можно упорядочить однократным применением одного из правил:
    1. Поменять местами два произвольных элемента массива;
    2. Изменить на обратный порядок произвольной последовательной цепочки элементов в массиве.
Если перестановки невозможны, или массив уже отсортирован - false.

Например, на входе

1) 1 3 2
Упорядочиваем правилом 1, меняем местами 3 и 2:
1 2 3

2) 3 2 1
Упорядочиваем правилом 2, меняем порядок с первого элемента до последнего:
1 2 3

3) 1 7 5 3 9
Упорядочиваем правилом 1, меняем местами 7 и 3:
1 3 5 7 9

4) 9 5 3 7 1
Нельзя упорядочить.

5) 1 4 3 2 5
Упорядочиваем правилом 2, меняем порядок с второго элемента до четвёртого:
1 2 3 4 5
"""

def str_from_list(data_list):
    """
    Функция выводит строку, состоящую из элементов списка.
    Будет использована для получения ключей для словаря комбинаций.
    """
    output = ""
    for i in data_list:
        output = "".join([output, str(i)])
    return output

def get_combos_rule_one(data):
    """Функция возвращает словарь всех комбинаций, которые можно получить по правилу 1."""
    tail_ind_cnt = len(data)-1
    ind_limit = len(data)
    combos = {str_from_list(data):data}
    while tail_ind_cnt > 0:
        curr_tail_ind = tail_ind_cnt
        curr_head_ind = 0
        while curr_tail_ind < ind_limit:
            temp_data = data.copy()
            new_head = temp_data[curr_tail_ind]
            temp_data[curr_tail_ind] = temp_data[curr_head_ind]
            temp_data[curr_head_ind] = new_head
            combos[str_from_list(temp_data)] = temp_data
            curr_tail_ind += 1
            curr_head_ind += 1
        tail_ind_cnt -= 1
    return combos

def rule_one(data):
    """Функция возвращает true, если массив можно упорядочить однократным применением правила 1"""
    sorted_key = str_from_list(sorted(data))
    if sorted_key in get_combos_rule_one(data):
        return True
    return False

def get_combo(data, head=0, tail=0):
    """
    Функция возвращает измененный список.
    В цепи эл-тов с индексами от head до tail включительно переставляются в обратном порядке.
    """
    new_data = data.copy()
    index_cnt = head
    for i in reversed(data[head:tail+1]):
        new_data[index_cnt] = i
        index_cnt += 1
    return new_data

def get_combos_rule_two(data):
    """Функция возвращает словарь всех комбинаций, которые можно получить по правилу 2."""
    tail_ind_cnt = len(data)-1
    ind_limit = len(data)
    combos = {str_from_list(data):data}
    while tail_ind_cnt > 0:
        curr_tail_ind = tail_ind_cnt
        curr_head_ind = 0
        while curr_tail_ind < ind_limit:
            temp_data = data.copy()
            combo = get_combo(temp_data, curr_head_ind, curr_tail_ind)
            combos[str_from_list(combo)] = combo
            curr_tail_ind += 1
            curr_head_ind += 1
        tail_ind_cnt -= 1
    return combos

def rule_two(data):
    """Функция возвращает true, если массив можно упорядочить однократным применением правила 2"""
    sorted_key = str_from_list(sorted(data))
    if sorted_key in get_combos_rule_two(data):
        return True
    return False

def Football(data, data_length): # pylint: disable=c0103
    """Функция по заданию"""
    if data_length > 1 and data != sorted(data):
        if rule_one(data) or rule_two(data):
            return True
    return False
