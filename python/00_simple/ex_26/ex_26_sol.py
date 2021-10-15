"""
Реализовать функцию white_walkers(inp_string)
Функция получает на вход строку и возвращает true или false.

Строка может быть пустой либо составленной из символов.

В строке могут присутствовать любые символы.

Числа в строке представлены цифрами от 0 до 9, при этом цепочек из цифр нет.
Т.е. строку вида '===123abcd' на вход функция точно не получит.

Функция возвращает True при условии:
в строке между каждой парой чисел, сумма которых равна 10, есть ровно три символа "=".

"axxb6===4xaf5===eee5" => true
"5==ooooooo=5=5" => false
"abc=7==hdjs=3gg1=======5" => true
"aaS=8" => false
"9===1===9===1===9" => true
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
