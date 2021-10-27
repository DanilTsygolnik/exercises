# pylint: disable=c0103
"""
Исходная строка string задается последовательностью из k нулей.
Алгоритм обрабатывает строку за k шагов.
На каждом i-ом шаге производится замена каждого i-го эл-та:
- если string[i]=0 --> замена 0 на 1;
- если string[i]=1 --> замена 1 на 0;
На k-ом шаге алгоритм обрабатывает последний эл-т и возвращает итоговую строку.

Основное задание: написать функцию Keymaker(int k), реализующую описанный алгоритм.

Доп. задание: выразить закономерность расположения единиц в итоговой строке от k в виде функции.
"""

def Keymaker(str_length):
    """Функция по заданию"""
    templ = str_length * [0]
    for i in range(1, str_length+1):
        elem_cnt = 1
        curr_index = 0
        while curr_index < str_length:
            if elem_cnt < i:
                elem_cnt += 1
            else:
                if templ[curr_index]==0:
                    templ[curr_index] = 1
                else:
                    templ[curr_index] = 0
                elem_cnt = 1
            curr_index += 1
    return "".join(str(i) for i in templ)

def Keymaker_math(str_length):
    """Функция по дополнительному заданию"""
    templ = str_length*[0]
    num_open = 10 * int(round(str_length**(1/2),1)) // 10
    for i in range(1, num_open+1):
        templ[i**2-1]=1
    return "".join(str(i) for i in templ)
