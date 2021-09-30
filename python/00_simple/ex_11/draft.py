#
#Условия:
#разность рассчитывается между целыми неотрицательными (Unsigned 32-bit integer [0 to 4 294 967 295] ??)
#строковые представления в диапазоне от 0 до 10^16 (включительно)
#на входе - всегда строка, состоящая только из цифр
#при составлении решения обойтись без использования поддержки BigInteger и сторонних библиотек
#
#Результат:
#Функция возвращает модуль разности (s1 - s2) в формате текстовой строки
#
#Пример:
#BigMinus("1234567891", "1") = "1234567890"
#BigMinus("1", "321") = "320"
#
#---
#
#"Возможно, в выбранном вами языке имеется поддержка BigInteger, однако в данной миссии надо обойтись без них.
#Придумайте, как вычислять разность для любых заданных значений"
#
#Т.е. расклад:
#Рассмотреть ситуацию, когда на вход функции поступает строка (число), не лежащее в диапазоне простых integers --> при переводе строки в целое число происходит переполнение (integer overflow)
#с учетом этого и нужно придумать, каким образом все же: 1) произвести вычетание чисел; 2) вывести строку с корректным ответом 
#
#----

def BigMinus(first_str, second_str):

    def big_num_small_num(first_str, second_str):
        if len(first_str) < len(second_str):
            big_n = second_str
            small_n = first_str
        elif len(first_str) > len(second_str):
            big_n = first_str 
            small_n = second_str
        else:
            if first_str < second_str:
                big_n = second_str
                small_n = first_str
            else:
                big_n = first_str 
                small_n = second_str
        return [big_n, small_n]

    def add_zeros(big_int, small_int):
        if len(big_int) > len(small_int):
            zeros_cnt = len(big_int) - len(small_int)
            zeros_str = zeros_cnt * '0'
            result = zeros_str + small_int
            return result
        else:
            return small_int

    # --------------------------------------------------
        
    integers = big_num_small_num(first_str, second_str)
    big_int = integers[0]
    small_int = integers[1]

    # если длины не равны, в короткую строку нужно добавить нули (один из вариантов)
    small_int = add_zeros(big_int, small_int)

    # при вычитании идем от последней цифры к первой
    subtract_results = []
    index_cnt = len(big_int) - 1
    imaginary_register = 0
    while index_cnt >= 0:
        i = int(big_int[index_cnt])
        j = int(small_int[index_cnt])
        result = imaginary_register + i - j
        #if i < j:
        if result < 0:
            result += 10
            imaginary_register = -1
        else:
            imaginary_register = 0
        subtract_results.append(str(result))  
        index_cnt -= 1
    output_str = ''
    index_cnt = len(subtract_results) - 1
    while index_cnt >= 0:
        output_str += subtract_results[index_cnt]
        index_cnt -= 1
    return output_str

print(BigMinus('11111', '111'))
