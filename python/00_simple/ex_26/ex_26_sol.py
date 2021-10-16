"""
Реализовать функцию white_walkers(inp_string)
Функция получает на вход строку и возвращает true или false.

Строка может быть пустой либо составленной из символов.

В строке могут присутствовать любые символы.

Числа в строке представлены цифрами от 0 до 9, при этом цепочек из цифр нет.
Т.е. строку вида '===123abcd' на вход функция точно не получит.

Функция возвращает True при условии:
в строке между каждой парой чисел, сумма которых равна 10, есть цепь из трех символов "=".

"axxb6===4xaf5===eee5" => true (2 пары, три знака '=' в 2/2)
"5==ooooooo=5=5" => false (2 пары, три знака '=' в 1/2)
"abc=7==hdjs=3gg1=======5" => true (1 пара, три знака '=' в 1/1)
"aaS=8" => false (0 пар)
"9===1===9===1===9" => true (4 пары, три знака '=' в 4/4)
"""


def get_pairs(string):
    """
    Функция выводит список вида [[a,b], [c,d], ...]].
    Список содержит пары чисел, которые задают интервалы между цифрами в string.
    """
    pairs = []
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
                pairs.append([head+1, tail])
            else:
                head = index_cnt
        index_cnt += 1
    return pairs

def chain_is_there(target, location, target_cnt=3):
    """
    Проверка на присутствие заданного кол-ва target'ов в строке.
    Функция возвращает True, если в интервале заданное кол-во найдено.
    По умолчанию, в соответствии с заданием, target_cnt=3.
    """
    cnt = 0
    for i in location:
        if i == target:
            cnt += 1
            if cnt == target_cnt:
                return True
    return False

#def white_walkers(string):
#    """Функция по заданию"""
#
#    numbers_pairs = get_pairs(string)
#    for i in numbers_pairs:
#        str_btw_numbers = string[i[0]:i[1]]
#    ...
#    return False
