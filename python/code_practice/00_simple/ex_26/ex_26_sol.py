"""
Реализовать функцию white_walkers(inp_string)
Функция получает на вход строку и возвращает true или false.

Строка может быть пустой либо составленной из символов.

В строке могут присутствовать любые символы.

Числа в строке представлены цифрами от 0 до 9, при этом цепочек из цифр нет.
Т.е. строку вида '===123abcd' на вход функция точно не получит.

Функция возвращает True при условии:
в строке между каждой парой чисел, сумма которых равна 10, есть три и более символов "=",
при этом их кол-во (для каждой пары чисел) должно быть кратно трем.

"axxb6===4xaf5===eee5" => true (2 пары, три знака '=' в 2/2)
"5==ooooooo=5=5" => false (2 пары, три знака '=' в 1/2)
"abc=7==hdjs=3gg1=======5" => true (1 пара, три знака '=' в 1/1)
"aaS=8" => false (0 пар)
"9===1===9===1===9" => true (4 пары, три знака '=' в 4/4)
"""


def get_all_pairs(string):
    """
    Функция выводит список вида [[a,b], [c,d], ...]].
    Список содержит пары цифр, между которыми осуществляется поиск "=".
    """
    pairs = []
    head = None
    tail = None
    numbers = {}
    for i in range(0,10):
        numbers[str(i)] = int(i)
    for i in string:
        if i in numbers:
            if head is not None:
                if tail is not None:
                    head = tail
                tail = i
                pairs.append([numbers[head], numbers[tail]])
            else:
                head = i
    return pairs

def get_all_indexes(string):
    """
    Функция выводит список вида [[a,b], [c,d], ...]].
    Список содержит пары чисел, которые задают интервалы между цифрами в string.
    """
    indexes = []
    head = None
    tail = None
    numbers = {}
    for i in range(0,10):
        numbers[str(i)] = i
    index_cnt = 0
    for i in string:
        if i in numbers:
            if head is not None:
                if tail is not None:
                    head = tail
                tail = index_cnt
                indexes.append([head+1, tail])
            else:
                head = index_cnt
        index_cnt += 1
    return indexes

def choose_pairs(string):
    """
    Функция возвращает список вида [[a,b], [c,d], ...]].
    Список содержит пары индексов для эл-тов all_pairs из string, сумма которых равна 10.
    """
    output = []
    all_pairs = get_all_pairs(string)
    all_indexes= get_all_indexes(string)
    for i, _ in enumerate(all_pairs):
        if all_pairs[i][0] + all_pairs[i][1] == 10:
            output.append(all_indexes[i])
    return output

def amount_is_there(target, location, target_cnt=3):
    """
    Проверка на присутствие заданного кол-ва target'ов в строке.
    Функция возвращает True, если в интервале заданное кол-во найдено.
    В соответствии с заданием target_cnt=3.
    """
    cnt = 0
    for i in location:
        if i == target:
            cnt += 1
    if cnt > 0 and cnt % target_cnt == 0:
        return True
    return False

def white_walkers(string):
    """Функция по заданию"""
    search_intervals = choose_pairs(string)
    if len(search_intervals) == 0:
        return False
    match_cnt = 0 # если кол-во совпадений совпадет с кол-вом пар чисел ==> True
    for i in search_intervals:
        if amount_is_there(target="=", location=string[i[0]:i[1]]):
            match_cnt += 1
    if match_cnt == len(search_intervals):
        return True
    return False
