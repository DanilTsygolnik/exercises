"""
Написать функцию Football(int F[], int N).

На вход функция получает массив F из N (N >= 1) целых неповторяющихся чисел. 
Функция возвращает true, если массив можно упорядочить однократным применением одного из правил: 
    1. Поменять местами два произвольных элемента массива;
    2. Изменить на обратный порядок произвольной последовательной цепочки элементов в массиве.

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
    output = ""
    for i in data_list:
        output = "".join([output, str(i)])
    return output

#def get_combos(data):
#    """
#    Функция возвращает словарь всех комбинаций, которые можно получить по правилу 1
#    """
#    tail_ind_cnt = len(data)-1
#    ind_limit = len(data)
#    combos = {}

